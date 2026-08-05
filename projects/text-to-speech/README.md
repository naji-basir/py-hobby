# Text-to-Speech

A small CLI application that converts text into an MP3 file using Google Text-to-Speech (`gTTS`).

## Features

- Interactive language selection
- Text input validation
- Saves output as `output/<filename>.mp3`
- Uses `gTTS`, `questionary`, and `rich`

## Requirements

- Python 3.12 or newer

## Installation

```powershell
cd projects\text-to-speech
uv install
```

## Usage

```powershell
uv run text-to-speech
```

Follow the prompts to select a language, type the text, and choose an output filename.

## Output

The tool creates an `output/` folder and saves the generated audio as `output/<filename>.mp3`.

## Project structure

- `src/text_to_speech/main.py` — interactive CLI runner.
- `src/text_to_speech/tts.py` — Google TTS wrapper.
- `pyproject.toml` — project metadata and dependencies.
