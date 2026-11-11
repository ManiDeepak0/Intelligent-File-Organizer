import tempfile
import unittest
from pathlib import Path
from core.scanner import scan_directory


class TestScanner(unittest.TestCase):
    def test_scan_returns_file_metadata(self):
        with tempfile.TemporaryDirectory() as temp:
            file_path = Path(temp) / "notes.txt"
            file_path.write_text("hello", encoding="utf-8")
            records = scan_directory(temp)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["name"], "notes.txt")
            self.assertEqual(records[0]["category"], "Documents")
            self.assertEqual(records[0]["size_bytes"], 5)


if __name__ == "__main__":
    unittest.main()
