# py-hobby

A small collection of Python mini-projects created for learning and experimentation.

## Projects

- **gemini-chat-bot** — Primary project: a Gemini-based chat bot (main project).
- **qr-generator** — A simple command-line QR code generator.
- **text-to-speech** — A CLI tool that converts text to MP3 using Google Text-to-Speech.
- **youtube-video-downloader** — A CLI tool for downloading YouTube videos or audio.

## Requirements

- Python 3.12 or newer
- `uv` installed and available on your PATH

## Quick start

### gemini-chat-bot

```powershell
cd projects\gemini-chat-bot
uv install
uv run gemini-chat-bot
```

Follow the prompts to configure and start the Gemini chat bot.

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

### youtube-video-downloader

Install `ffmpeg` before running this project. On Windows, you can install it with:

```powershell
winget install Gyan.FFmpeg
```

Then install the project dependencies and start the downloader:

```powershell
cd projects\youtube-video-downloader
uv sync
uv run youtube-video-downloader
```

Follow the prompts to enter a YouTube URL and choose whether to download a video or audio. Files are saved to the Windows `Downloads` folder.

## Notes

- Each project has its own `README.md` with project-specific instructions.
- The source for each project is located under `projects/<project-name>/src/`.
