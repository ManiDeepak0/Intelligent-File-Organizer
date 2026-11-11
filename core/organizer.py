from pathlib import Path
from core.file_manager import move_file, unique_destination, save_operation_history
from utils.file_categories import categorize_file


def organize_directory(directory: str | Path, dry_run: bool = False,
                       recursive: bool = False, history_file: str = "history/operations.json") -> list[dict]:
    """Move files into category folders. Existing category folders are not reprocessed."""
    root = Path(directory).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Not a valid directory: {root}")

    iterator = root.rglob("*") if recursive else root.iterdir()
    candidates = []
    for path in iterator:
        if not path.is_file():
            continue
        # Avoid moving files already inside a category directory at the root.
        if path.parent != root and not recursive:
            continue
        if path.parent.name in {"Documents", "Images", "Videos", "Audio", "Archives",
                                "Code", "Spreadsheets", "Presentations", "Executables", "Others"}:
            continue
        candidates.append(path)

    results, history_entries = [], []
    for source in sorted(candidates, key=lambda p: str(p).lower()):
        category = categorize_file(source)
        target_dir = root / category
        destination = unique_destination(target_dir / source.name)
        if dry_run:
            results.append({"source": str(source), "destination": str(destination), "category": category, "status": "preview"})
            continue
        try:
            moved_to = move_file(source, destination)
            results.append({"source": str(source), "destination": str(moved_to), "category": category, "status": "moved"})
            history_entries.append({"source": str(source), "destination": str(moved_to)})
        except OSError as exc:
            results.append({"source": str(source), "destination": str(destination), "category": category,
                            "status": f"error: {exc}"})

    if history_entries:
        save_operation_history(history_entries, history_file)
    return results
