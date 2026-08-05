# py-hobby

A small collection of Python mini-projects created for learning and experimentation.

## Projects

- **qr-generator** — A simple command-line QR code generator.
- **text-to-speech** — A CLI tool that converts text to MP3 using Google Text-to-Speech.

## Requirements

- Python 3.12 or newer
- `uv` installed and available on your PATH

## Quick start

### qr-generator

```powershell
cd projects\qr-generator
uv install
uv run qr-generator
```

Enter the text or URL when prompted. The QR code is saved as `qrcode.png` in the current folder.

### text-to-speech

```powershell
cd projects\text-to-speech
uv install
uv run text-to-speech
```

Follow the prompts to choose a language, enter text, and name the output file. The generated MP3 is saved under `output/`.

## Notes

- Each project has its own `README.md` with project-specific instructions.
- The source for each project is located under `projects/<project-name>/src/`.
