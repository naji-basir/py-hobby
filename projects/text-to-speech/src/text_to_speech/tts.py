from pathlib import Path

from gtts import gTTS  # type: ignore


def text_to_speech(
    text: str,
    language: str,
    filename: str,
) -> Path:
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"{filename}.mp3"

    tts = gTTS(
        text=text,
        lang=language,
    )
    tts.save(str(output_path))

    return output_path
