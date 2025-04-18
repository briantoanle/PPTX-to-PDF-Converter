# 🖨️ PPTX to PDF Converter (macOS)

A Python script to batch convert `.pptx` (PowerPoint) files to `.pdf` format using **LibreOffice** in headless mode.

## 📦 Requirements

- Python 3 (pre-installed on macOS)
- [LibreOffice](https://www.libreoffice.org/) (must be installed and accessible at `/Applications/LibreOffice.app`)

Install LibreOffice via [Homebrew](https://brew.sh/):
```bash
brew install --cask libreoffice
```

## 📝 Script Features

- Converts all `.pptx` files in a specified folder to `.pdf`
- Uses LibreOffice's `--headless` mode (no GUI)
- Works with folders and filenames that contain spaces

## 🚀 Usage

### 1. Save the script as `pptx_to_pdf.py`

### 2. Run from Terminal with a folder path:
```bash
python3 pptx_to_pdf.py "/path/to/your/folder"
```

### Example:
```bash
python3 pptx_to_pdf.py "/Users/yourname/Documents/Presentations"
```

Converted PDFs will appear in the same folder as the original `.pptx` files.

## 📂 Script Behavior

- Ignores non-`.pptx` files
- Overwrites existing `.pdf` files with the same name if they exist

## ⚠️ Notes

- LibreOffice must be installed at the default macOS location:
  ```
  /Applications/LibreOffice.app
  ```
- No internet connection required
- Works only on macOS
