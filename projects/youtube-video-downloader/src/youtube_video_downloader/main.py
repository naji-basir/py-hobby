from pathlib import Path

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from youtube_video_downloader.downloader import (
    download_media,
    get_video_info,
)
from youtube_video_downloader.formats import get_available_heights
from youtube_video_downloader.progress import DownloadProgress
from youtube_video_downloader.utils import (
    format_duration,
    is_youtube_url,
)

console = Console()


def show_header() -> None:
    """Show the application name and a short description."""
    console.print(
        Panel(
            Text.from_markup(
                "[bold cyan]YouTube Video Downloader[/bold cyan]\n"
                "[dim]Download videos and audio using yt-dlp[/dim]"
            ),
            border_style="cyan",
            padding=(1, 2),
        )
    )


def main() -> None:
    # Start with a simple header so the user knows what the program does.
    show_header()

    # Ask the user for the YouTube URL they want to download.
    url = console.input("[bold cyan]YouTube URL:[/bold cyan] ").strip()

    # Stop early if the user didn't enter anything.
    if not url:
        console.print("[bold yellow]⚠ Please enter a YouTube URL.[/bold yellow]")
        return

    # This application is intentionally limited to YouTube URLs.
    if not is_youtube_url(url):
        console.print("[bold red]✗ Only YouTube URLs are supported.[/bold red]")
        return

    # Fetch the video's metadata before asking the user what to download.
    # The spinner gives the user feedback while yt-dlp communicates with YouTube.
    with console.status(
        "[bold cyan]Fetching video information...[/bold cyan]",
        spinner="dots",
    ):
        try:
            info = get_video_info(url)

            # Find the video qualities that are actually available.
            heights = get_available_heights(info)

        except Exception as error:
            # yt-dlp can fail for many reasons, such as an unavailable video,
            # network problems, or YouTube changing its response.
            console.print(
                Panel(
                    f"[red]{error}[/red]",
                    title="[bold red]Error[/bold red]",
                    border_style="red",
                )
            )
            return

    # Show the user some basic information so they can confirm
    # that they entered the correct video.
    console.print(
        Panel(
            f"[bold white]Title:[/bold white] "
            f"[cyan]{info.title}[/cyan]\n"
            f"[bold white]Channel:[/bold white] "
            f"[green]{info.uploader or 'Unknown'}[/green]\n"
            f"[bold white]Duration:[/bold white] "
            f"[yellow]{format_duration(info.duration)}[/yellow]",
            title="[bold cyan]Video Information[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )

    # Let the user decide whether they want the video or only the audio.
    action = questionary.select(
        "What do you want to download?",
        choices=[
            "Video",
            "Audio",
            "Cancel",
        ],
    ).ask()

    # The user can cancel at any point without causing an error.
    if action == "Cancel" or action is None:
        console.print("[dim]Cancelled.[/dim]")
        return

    # ---------------------------------------------------------
    # Video download
    # ---------------------------------------------------------

    if action == "Video":
        # A video needs at least one available video quality.
        if not heights:
            console.print("[bold red]✗ No compatible video formats found.[/bold red]")
            return

        # Show the available qualities from highest to lowest.
        quality = questionary.select(
            "Select video quality:",
            choices=[f"{height}p" for height in heights],
        ).ask()

        if quality is None:
            console.print("[dim]Cancelled.[/dim]")
            return

        # Convert "720p" into the integer 720 because yt-dlp
        # needs the height as a number when selecting the format.
        selected_height = int(quality.removesuffix("p"))

        media_type = "video"

        # This value is not used for video downloads, but keeping
        # a default value makes the download function easier to call.
        audio_format = "mp3"

    # ---------------------------------------------------------
    # Audio download
    # ---------------------------------------------------------

    else:
        # Ask which audio format the user wants.
        audio_format = questionary.select(
            "Select audio format:",
            choices=[
                "mp3",
                "m4a",
                "wav",
            ],
        ).ask()

        if audio_format is None:
            console.print("[dim]Cancelled.[/dim]")
            return

        # Audio downloads don't need a video height.
        selected_height = None
        media_type = "audio"

    # Save downloaded files directly to the user's Windows
    # Downloads folder instead of the project directory.
    download_dir = Path.home() / "Downloads"

    console.print()

    # Start the download and show live progress in the terminal.
    try:
        with DownloadProgress() as progress:
            download_media(
                url,
                download_dir,
                media_type=media_type,
                height=selected_height,
                audio_format=audio_format,
                progress_hook=progress.hook,
            )

    except Exception as error:
        # Show a clean error message instead of exposing an
        # unnecessary Python traceback to the user.
        console.print(
            Panel(
                f"[red]{error}[/red]",
                title="[bold red]Download Failed[/bold red]",
                border_style="red",
            )
        )
        return

    # Tell the user that yt-dlp finished successfully and
    # where they can find the downloaded file.
    console.print(
        Panel(
            "[bold green]✓ Download completed successfully![/bold green]\n\n"
            f"[bold]Location:[/bold] "
            f"[cyan]{download_dir}[/cyan]",
            title="[bold green]Success[/bold green]",
            border_style="green",
        )
    )


# Only run the application when this file is executed directly.
# This prevents main() from running if the module is imported elsewhere.
if __name__ == "__main__":
    main()
