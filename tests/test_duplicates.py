import tempfile
import unittest
from pathlib import Path
from core.duplicate_finder import find_duplicates


class TestDuplicates(unittest.TestCase):
    def test_finds_identical_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "one.txt").write_text("same", encoding="utf-8")
            (root / "two.txt").write_text("same", encoding="utf-8")
            groups = find_duplicates(root)
            self.assertEqual(len(groups), 1)
            self.assertEqual(len(groups[0]["files"]), 2)


if __name__ == "__main__":
    unittest.main()
