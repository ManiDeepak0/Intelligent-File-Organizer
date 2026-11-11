from pathlib import Path
from datetime import datetime
from utils.file_categories import categorize_file


def scan_directory(directory: str | Path, recursive: bool = False) -> list[dict]:
    """Return metadata for files in a directory without modifying them."""
    root = Path(directory).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Not a valid directory: {root}")

    iterator = root.rglob("*") if recursive else root.iterdir()
    records = []
    for path in iterator:
        if not path.is_file():
            continue
        try:
            stat = path.stat()
            records.append({
                "name": path.name,
                "path": str(path.resolve()),
                "extension": path.suffix.lower() or "[no extension]",
                "category": categorize_file(path),
                "size_bytes": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
            })
        except OSError:
            # Skip files that disappear or become inaccessible during a scan.
            continue
    return sorted(records, key=lambda item: item["path"].lower())
