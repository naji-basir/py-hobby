from youtube_video_downloader.models import VideoInfo


def get_available_heights(info: VideoInfo) -> list[int]:
    available_heights = {
        fmt["height"]
        for fmt in info.formats
        if fmt.get("vcodec") != "none" and fmt.get("height")
    }

    return sorted(available_heights, reverse=True)
