from pathlib import Path
import json
import shutil
from datetime import datetime, timezone


def unique_destination(destination: str | Path) -> Path:
    """Return a non-existing path, adding a numbered suffix if needed."""
    destination = Path(destination)
    if not destination.exists():
        return destination
    parent, stem, suffix = destination.parent, destination.stem, destination.suffix
    counter = 1
    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def move_file(source: str | Path, destination: str | Path) -> Path:
    source, destination = Path(source), Path(destination)
    if not source.is_file():
        raise FileNotFoundError(f"Source file does not exist: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination = unique_destination(destination)
    shutil.move(str(source), str(destination))
    return destination


def save_operation_history(entries: list[dict], history_file: str | Path) -> None:
    history_path = Path(history_file)
    history_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        history = json.loads(history_path.read_text(encoding="utf-8")) if history_path.exists() else []
    except (json.JSONDecodeError, OSError):
        history = []
    history.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operations": entries,
    })
    history_path.write_text(json.dumps(history, indent=2), encoding="utf-8")


def undo_last_operation(history_file: str | Path = "history/operations.json") -> int:
    history_path = Path(history_file)
    if not history_path.exists():
        raise FileNotFoundError("No operation history found.")

    history = json.loads(history_path.read_text(encoding="utf-8"))
    if not history:
        raise ValueError("There are no operations to undo.")

    last = history[-1]
    restored = 0
    for item in reversed(last.get("operations", [])):
        source = Path(item["source"])
        destination = Path(item["destination"])
        if not destination.exists():
            continue
        if source.exists():
            # Do not overwrite a file created after the original operation.
            continue
        source.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(destination), str(source))
        restored += 1

    history.pop()
    history_path.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return restored
