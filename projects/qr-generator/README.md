# QR Generator

A lightweight CLI utility to generate QR codes from text or URLs.

## Features

- Generates a QR code from user-provided text or URL
- Saves output as `qrcode.png`
- Uses `qrcode` and `Pillow`

## Requirements

- Python 3.12 or newer

## Installation

```powershell
cd projects\qr-generator
uv install
```

## Usage

```powershell
uv run qr-generator
```

Then enter the text or URL when prompted. The QR code is saved as `qrcode.png` in the current folder.

## Project structure

- `src/qr_generator/main.py` — CLI entry point.
- `src/qr_generator/generator.py` — QR generation helper.
- `pyproject.toml` — project metadata and dependencies.
