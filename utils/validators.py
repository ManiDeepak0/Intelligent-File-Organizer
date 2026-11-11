from pathlib import Path


def validate_directory(directory: str | Path) -> Path:
    path = Path(directory).expanduser().resolve()
    if not path.exists():
        raise ValueError(f"Directory does not exist: {path}")
    if not path.is_dir():
        raise ValueError(f"Path is not a directory: {path}")
    return path
