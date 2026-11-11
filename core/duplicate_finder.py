
from pathlib import Path
import hashlib
from collections import defaultdict


def calculate_file_hash(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Calculate SHA-256 hash of a file."""

    digest = hashlib.sha256()

    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            digest.update(chunk)

    return digest.hexdigest()


def find_duplicates(directory: str | Path, recursive: bool = False) -> list[dict]:
    """Find duplicate files using SHA-256 hashing."""

    root = Path(directory).expanduser().resolve()

    if not root.exists() or not root.is_dir():
        raise ValueError(f"Not a valid directory: {root}")

    iterator = root.rglob("*") if recursive else root.iterdir()

    by_size = defaultdict(list)

    # Group files by size
    for path in iterator:
        if path.is_file():
            try:
                by_size[path.stat().st_size].append(path)
            except OSError:
                continue

    by_hash = defaultdict(list)

    # Calculate hashes only for files having matching sizes
    for same_size_files in by_size.values():

        if len(same_size_files) < 2:
            continue

        for path in same_size_files:
            try:
                file_hash = calculate_file_hash(path)
                by_hash[file_hash].append(str(path.resolve()))

            except OSError:
                continue

    # Return duplicate groups
    duplicates = [
        {
            "sha256": file_hash,
            "files": sorted(paths)
        }
        for file_hash, paths in by_hash.items()
        if len(paths) > 1
    ]

    return sorted(duplicates, key=lambda item: item["files"][0].lower())
