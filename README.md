# Web Recon Tool - Interesting File Grabber

This Python 3 tool automates the discovery and download of potentially sensitive files from a target website. It focuses on fetching `.js`, `.json`, `.xml`, `.config`, `.conf`, and `.env` files by scanning the HTML for linked resources.

## 🔍 Features

- Extracts and downloads:
  - JavaScript files (`.js`)
  - Configuration and data files ( `.json`, `.xml`, `.config`, `.conf`, `.env` )
- Creates organized output:
  - Files saved in `download/<target-domain>/` directory
- Handles both relative and absolute URLs
- Logs progress and errors cleanly to the console

## 📁 Directory Structure

```
web_recon_tool/
├── grab_files.py        # Main script
└── download/
    └── example.com/
        ├── app.js
        ├── config.json
        └── sitemap.xml
```

## 🚀 Usage

1. **Install dependencies** (if needed):

```bash
pip install requests beautifulsoup4
```

2. **Run the script:**

```bash
python3 grab_files.py
```

3. **Enter the target URL** when prompted, e.g.:

```
Enter target URL (e.g. https://example.com): https://example.com
```

4. Files will be saved under `download/example.com/`.

## ⚠️ Legal Disclaimer

This tool is intended **for educational and authorized security testing only**. Do **not** use it on systems or websites you do not own or have explicit permission to test.

## 📌 Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`

