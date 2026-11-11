import tempfile
import unittest
from pathlib import Path
from core.organizer import organize_directory


class TestOrganizer(unittest.TestCase):
    def test_organize_moves_file_to_category(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "photo.jpg"
            source.write_bytes(b"image")
            results = organize_directory(root, history_file=root / "history.json")
            self.assertEqual(results[0]["status"], "moved")
            self.assertTrue((root / "Images" / "photo.jpg").exists())
            self.assertFalse(source.exists())


if __name__ == "__main__":
    unittest.main()
