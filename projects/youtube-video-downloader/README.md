# YouTube Video Downloader

A simple and user-friendly command-line YouTube downloader built with Python, `yt-dlp`, Rich, and Questionary.

The application runs directly in the terminal and allows you to download:

- 🎬 YouTube videos
- 🎵 YouTube audio
- 🎚️ Videos in different available qualities
- 🎧 Audio in MP3, M4A, or WAV
- 📁 Files directly to the Windows `Downloads` folder

> **Note:** This project is designed specifically for YouTube URLs.

---

## Features

- 🎬 Download YouTube videos
- 🎵 Download audio only
- 🎚️ Select available video quality
- 🎧 Select audio format
- 📊 Live download progress
- ⏳ Loading indicators while fetching video information
- 🌈 Clean and colorful terminal interface
- 🛡️ YouTube URL validation
- 📁 Automatically saves files to the Windows `Downloads` folder
- 🔄 Retry support for unstable connections
- 🚫 Playlist downloads are disabled
- 🧹 Temporary video/audio files are merged and cleaned automatically by `ffmpeg`

---

## Tech Stack

- **Python**
- **uv** — Python project and package manager
- **yt-dlp** — YouTube media extraction and downloading
- **FFmpeg** — Video/audio merging and conversion
- **Rich** — Terminal UI, panels, colors, and progress bars
- **Questionary** — Interactive terminal prompts

---

## Project Structure

```text
youtube-video-downloader/
│
├── src/
│   └── youtube_video_downloader/
│       ├── __init__.py
│       ├── main.py
│       ├── downloader.py
│       ├── formats.py
│       ├── models.py
│       ├── progress.py
│       └── utils.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md

```

## Installation

### 1. Install Python

Check your Python version:

```bash
python --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

### 2. Install uv

On Windows:

```powershell
winget install astral-sh.uv
```

Verify:

```powershell
uv --version
```

### 3. Install FFmpeg

On Windows:

```powershell
winget install Gyan.FFmpeg
```

Restart your terminal after installation and verify:

```powershell
ffmpeg -version
```

## Project Setup

Clone the repository:

```bash
git clone https://github.com/naji-basir/py-hobby.git
```

Enter the project directory:

```bash
cd youtube-video-downloader
```

Install dependencies:

```bash
uv sync
```

## Run

Start the application:

```bash
uv run youtube-video-downloader
```

Or run it as a Python module:

```bash
uv run python -m youtube_video_downloader.main
```

After the initial setup, simply run:

```bash
uv run youtube-video-downloader
```

## Usage

Enter a YouTube URL:

```text
YouTube URL: https://youtu.be/XXXXXXXXXXX
```

Choose what to download:

```text
? What do you want to download?
❯ Video
  Audio
  Cancel
```

### Video

Select the available quality:

```text
? Select video quality:
❯ 1080p
  720p
  480p
  360p
```

### Audio

Select the audio format:

```text
? Select audio format:
❯ mp3
  m4a
  wav
```

## Download Location

Files are automatically saved to the Windows `Downloads` folder:

```text
C:\Users\<Username>\Downloads
```

## Project Structure

```text
youtube-video-downloader/
│
├── src/
│   └── youtube_video_downloader/
│       ├── __init__.py
│       ├── main.py
│       ├── downloader.py
│       ├── formats.py
│       ├── models.py
│       ├── progress.py
│       └── utils.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Development

Install dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run youtube-video-downloader
```

Run directly through Python:

```bash
uv run python -m youtube_video_downloader.main
```

## Update Dependencies

```bash
uv lock --upgrade
uv sync
```

## Troubleshooting

### FFmpeg not found

Install FFmpeg:

```powershell
winget install Gyan.FFmpeg
```

Restart the terminal and verify:

```powershell
ffmpeg -version
```

### yt-dlp issues

Update the dependencies:

```bash
uv lock --upgrade
uv sync
```

## Legal Notice

This project is intended for educational and personal use.

Only download content that you have permission or legal rights to download.

Respect YouTube's Terms of Service, copyright laws, licenses, and content creators' rights.

## Author

**Naji Basir**

Part of the `py-hobby` collection.
