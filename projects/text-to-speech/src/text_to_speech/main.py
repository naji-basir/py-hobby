import questionary  # type: ignore
from rich.console import Console  # type: ignore
from rich.panel import Panel  # type: ignore

from text_to_speech.tts import text_to_speech

console = Console()
languages = {"en": "English", "ar": "Arabic"}


def main() -> None:
    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]🎤 Text to Speech[/bold cyan]\n"
            "[green]Convert text into MP3 using Google Text-to-Speech[/green]",
            border_style="cyan",
        )
    )

    language = questionary.select(
        "Select a language:",
        choices=[
            questionary.Choice(title=name, value=code)
            for code, name in sorted(
                languages.items(),
                key=lambda item: item[1],
            )
        ],
    ).ask()

    if language is None:
        console.print("[yellow]Operation cancelled.[/yellow]")
        return

    text = questionary.text(
        "Enter the text:",
        validate=lambda value: bool(value.strip()) or "Text cannot be empty.",
    ).ask()

    if text is None:
        console.print("[yellow]Operation cancelled.[/yellow]")
        return

    filename = questionary.text(
        "Output filename:",
        default="speech",
    ).ask()

    if filename is None:
        console.print("[yellow]Operation cancelled.[/yellow]")
        return

    console.print()
    console.print("[cyan]Generating speech...[/cyan]")

    output_file = text_to_speech(
        text=text,
        language=language,
        filename=filename,
    )

    console.print()
    console.print(
        f"[bold green]✓ Success![/bold green] Audio saved to [yellow]{output_file}[/yellow]"
    )


if __name__ == "__main__":
    main()
