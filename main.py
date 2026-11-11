from __future__ import annotations

import argparse
from pathlib import Path

from core.scanner import scan_directory
from core.organizer import organize_directory
from core.duplicate_finder import find_duplicates
from core.file_manager import undo_last_operation
from reports.report_generator import generate_scan_report, generate_organization_report
from utils.logger import setup_logger
from utils.validators import validate_directory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="SWYNEX Intelligent File Organizer - scan, organize and detect duplicate files."
    )
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Scan a directory and generate a report.")
    scan.add_argument("directory", help="Directory to scan.")
    scan.add_argument("--output", default="reports/scan_report.csv", help="CSV report path.")

    organize = sub.add_parser("organize", help="Organize files into category folders.")
    organize.add_argument("directory", help="Directory to organize.")
    organize.add_argument("--dry-run", action="store_true", help="Preview changes without moving files.")
    organize.add_argument("--recursive", action="store_true", help="Include files in subdirectories.")
    organize.add_argument("--report", default="reports/organization_report.csv", help="CSV report path.")

    duplicates = sub.add_parser("duplicates", help="Find duplicate files using SHA-256.")
    duplicates.add_argument("directory", help="Directory to search.")
    duplicates.add_argument("--recursive", action="store_true")
    duplicates.add_argument("--output", default="reports/duplicates_report.csv")

    undo = sub.add_parser("undo", help="Undo the most recent organization operation.")
    undo.add_argument("--history", default="history/operations.json")

    return parser


def main() -> None:
    args = build_parser().parse_args()
    logger = setup_logger(args.log_level)

    try:
        if args.command == "undo":
            restored = undo_last_operation(args.history)
            print(f"Undo completed. Restored {restored} file(s).")
            return

        directory = validate_directory(args.directory)

        if args.command == "scan":
            records = scan_directory(directory)
            output = generate_scan_report(records, args.output)
            print(f"Scanned {len(records)} file(s). Report: {output}")

        elif args.command == "organize":
            result = organize_directory(directory, dry_run=args.dry_run, recursive=args.recursive)
            output = generate_organization_report(result, args.report)
            moved = sum(1 for item in result if item["status"] == "moved")
            print(f"{'Previewed' if args.dry_run else 'Organized'} {len(result)} file(s); moved {moved}.")
            print(f"Report: {output}")
            if args.dry_run:
                print("Dry run only: no files were changed.")

        elif args.command == "duplicates":
            groups = find_duplicates(directory, recursive=args.recursive)
            output = args.output
            from reports.report_generator import generate_duplicate_report
            generate_duplicate_report(groups, output)
            duplicate_count = sum(len(group["files"]) - 1 for group in groups)
            print(f"Found {len(groups)} duplicate group(s), {duplicate_count} extra copy/copies.")
            print(f"Report: {output}")

    except (ValueError, OSError) as exc:
        logger.error("%s", exc)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
