from collections.abc import Callable
from pathlib import Path
from typing import Any

import yt_dlp

from youtube_video_downloader.models import VideoInfo


def download_media(
    url: str,
    download_dir: Path,
    media_type: str,
    height: int | None = None,
    audio_format: str = "mp3",
    progress_hook: Callable[[dict[str, Any]], None] | None = None,
) -> None:

    if media_type == "video":
        if height:
            format_selector = (
                f"bestvideo[height<={height}]+bestaudio/best[height<={height}]"
            )

            output_template = str(download_dir / f"%(title)s_{height}p.%(ext)s")

        else:
            format_selector = "bestvideo+bestaudio/best"

            output_template = str(download_dir / "%(title)s.%(ext)s")

        options = {
            "format": format_selector,
            "outtmpl": output_template,
            "merge_output_format": "mp4",
        }

    elif media_type == "audio":
        output_template = str(download_dir / "%(title)s_audio.%(ext)s")

        options = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": audio_format,
                    "preferredquality": "192",
                }
            ],
        }

    else:
        raise ValueError(f"Unsupported media type: {media_type}")

    options.update(
        {
            "noplaylist": True,
            "socket_timeout": 30,
            "retries": 10,
            "fragment_retries": 10,
            "quiet": True,
            "no_warnings": True,
            "noprogress": True,
            "progress_hooks": ([progress_hook] if progress_hook else []),
        }
    )

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def get_video_info(url: str) -> VideoInfo:
    options = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)

    return VideoInfo(
        title=info["title"],
        uploader=info.get("uploader"),
        duration=info.get("duration"),
        webpage_url=info["webpage_url"],
        formats=info.get("formats", []),
    )
