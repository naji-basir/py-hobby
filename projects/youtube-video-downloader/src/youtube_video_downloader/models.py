from dataclasses import dataclass


@dataclass
class VideoInfo:
    title: str
    uploader: str | None
    duration: int | None
    webpage_url: str
    formats: list[dict]
