from pathlib import Path
import csv


def _write_csv(rows: list[dict], output_path: str | Path, fieldnames: list[str]) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return output.resolve()


def generate_scan_report(records: list[dict], output_path: str | Path) -> Path:
    fields = ["name", "path", "extension", "category", "size_bytes", "modified"]
    return _write_csv(records, output_path, fields)


def generate_organization_report(records: list[dict], output_path: str | Path) -> Path:
    fields = ["source", "destination", "category", "status"]
    return _write_csv(records, output_path, fields)


def generate_duplicate_report(groups: list[dict], output_path: str | Path) -> Path:
    rows = []
    for group in groups:
        for file_path in group["files"]:
            rows.append({"sha256": group["sha256"], "file": file_path,
                         "duplicate_count": len(group["files"])})
    return _write_csv(rows, output_path, ["sha256", "file", "duplicate_count"])
