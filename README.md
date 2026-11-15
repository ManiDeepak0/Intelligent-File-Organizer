
<div align="center">

# 🚀 SWYNEX Intelligent File Organizer

### Organize Smarter. Manage Better. Save Time.

A powerful Python-based CLI application that automatically organizes files, detects duplicates using SHA-256 hashing, manages directories, and generates detailed reports.

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-555555?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Active-success?style=for-the-badge)

**Developed by Mani Deepak Chivukula**

**Python Development Internship | SWYNEX Technologies**

</div>

---

## 📌 Overview

Managing hundreds of files manually can be time-consuming and frustrating.

**SWYNEX Intelligent File Organizer** solves this problem through Python automation. It scans directories, identifies file types, automatically categorizes files, detects duplicate content, and generates organized reports.

The application provides a simple command-line interface with safe file operations, input validation, logging, and operation history.

## ✨ Key Features

| Feature | Description |
|---|---|
| 📂 Automatic Organization | Sorts files into categorized folders |
| 🔍 Duplicate Detection | Identifies identical files using SHA-256 |
| 📁 Custom Folders | Creates user-defined folders |
| 📊 File Reports | Generates CSV and JSON reports |
| 🔄 Undo Operations | Restores files from the latest recorded operation |
| 🕒 Operation History | Tracks previous organization activities |
| 👀 Dry Run Mode | Previews file movements before execution |
| 🛡️ Safe File Handling | Prevents accidental overwriting |
| 📝 Logging | Records activities and errors |
| 🧪 Unit Testing | Tests functionality using Pytest |

## 🖥️ Application Preview

<!-- Add your actual application screenshot here -->

<div align="center">

<!-- Replace the URL below with your GitHub screenshot URL -->

<img src="assets\preview.png" alt="SWYNEX Intelligent File Organizer CLI" width="850"/>

*Command-line interface preview*

</div>

## ⚙️ How It Works

```text
          INPUT DIRECTORY
                 |
                 ▼
          FILE SCANNING
                 |
                 ▼
        EXTENSION DETECTION
                 |
                 ▼
         FILE CATEGORIZATION
                 |
          ┌──────┴──────┐
          ▼             ▼
    ORGANIZATION    DUPLICATE
       ENGINE       DETECTION
          |             |
          ▼             ▼
    CATEGORY        SHA-256
     FOLDERS         HASHING
          |             |
          └──────┬──────┘
                 ▼
          REPORT GENERATION
                 |
                 ▼
          CSV / JSON REPORTS
```

## 🗂️ Supported File Categories

| Category | Extensions |
|---|---|
| Documents | PDF, DOC, DOCX, TXT, PPT, PPTX |
| Images | JPG, JPEG, PNG, GIF, BMP, SVG, WEBP |
| Videos | MP4, MKV, AVI, MOV, WMV |
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Spreadsheets | XLS, XLSX, CSV |
| Code | PY, JAVA, JS, HTML, CSS, CPP, SQL |
| Others | Unrecognized extensions |

## 🛠️ Tech Stack

**Programming Language**
- Python 3.10+

**Python Modules**
- `pathlib` – File and directory management
- `os` – Operating system operations
- `shutil` – File moving and copying
- `hashlib` – SHA-256 hashing
- `datetime` – File timestamps
- `json` – JSON reports and history
- `csv` – CSV report generation
- `logging` – Application logging
- `argparse` – Command-line arguments
- `collections` – Data grouping and counting

**Testing**
- Pytest

**Development Tools**
- Visual Studio Code
- Git
- GitHub

## 📁 Project Structure

```text
SWYNEX-Intelligent-File-Organizer/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── core/
│   ├── scanner.py
│   ├── organizer.py
│   ├── duplicate_finder.py
│   └── file_manager.py
│
├── utils/
│   ├── file_categories.py
│   ├── validators.py
│   └── logger.py
│
├── reports/
│   └── report_generator.py
│
├── history/
├── logs/
│
└── tests/
    ├── test_scanner.py
    ├── test_organizer.py
    └── test_duplicates.py
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SWYNEX-Intelligent-File-Organizer.git
```

### 2. Navigate to the project

```bash
cd SWYNEX-Intelligent-File-Organizer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows CMD**

```cmd
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

All commands should be executed from the project root directory.

### 1. View available commands

```bash
python main.py --help
```

### 2. Scan a directory

```bash
python main.py scan "C:\SampleFiles"
```

### 3. Preview file organization

```bash
python main.py organize "C:\SampleFiles" --dry-run
```

### 4. Organize files automatically

```bash
python main.py organize "C:\SampleFiles"
```

### 5. Detect duplicate files

```bash
python main.py duplicates "C:\SampleFiles"
```

### 6. Generate file reports

```bash
python main.py report "C:\SampleFiles"
```

### 7. Create a custom folder

```bash
python main.py create-folder "C:\SampleFiles" Projects
```

### 8. View operation history

```bash
python main.py history
```

### 9. Undo the last operation

```bash
python main.py undo
```

## 📊 Generated Reports

The application generates detailed reports containing file information and category statistics.

**CSV Report**

`reports/file_report.csv`

**JSON Report**

`reports/file_report.json`

Report information includes:

- Total number of files
- File names and extensions
- File sizes
- Modification dates
- File categories
- Category distribution
- Total storage size

## 🧪 Testing

Run all unit tests:

```bash
pytest -v
```

Run individual test modules:

```bash
pytest tests/test_scanner.py -v
```

```bash
pytest tests/test_organizer.py -v
```

```bash
pytest tests/test_duplicates.py -v
```

## 🔐 Safety and Reliability

- Dry-run mode allows users to preview file movements.
- SHA-256 detects duplicate content without relying on filenames.
- Duplicate files are never automatically deleted.
- Existing destination files are protected against overwriting.
- Operation history supports undo functionality.
- Input validation and exception handling help prevent unexpected failures.

**Recommendation:** Test the application using sample directories and keep backups of important files before performing file operations.

## 🔮 Future Enhancements

- Advanced interactive terminal dashboard
- File filtering by size and modification date
- Improved recovery for interrupted operations
- More detailed storage analytics
- Configurable file categories
- Advanced duplicate management

## 👨‍💻 Author

**Mani Deepak Chivukula**

Python Developer | AI & Data Science Graduate

📌 Internship: SWYNEX Technologies

🔗 [GitHub Profile](https://github.com/YOUR_USERNAME)

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

<div align="center">

**Built with ❤️ using Python**

*Intelligent File Organizer*

</div>
