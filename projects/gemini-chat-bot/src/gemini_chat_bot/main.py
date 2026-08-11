from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from .gemini import GeminiChat

console = Console()


def show_welcome() -> None:
    console.print(
        Panel.fit(
            "[bold cyan]Gemini Chatbot[/bold cyan]\n"
            "[dim]Powered by Google Gemini API[/dim]\n\n"
            "Type [bold]/help[/bold] to see available commands.",
            border_style="cyan",
        )
    )


def show_help() -> None:
    console.print(
        Panel(
            "[bold]/help[/bold]    Show available commands\n"
            "[bold]/clear[/bold]   Clear conversation history\n"
            "[bold]/history[/bold] Show conversation history\n"
            "[bold]/exit[/bold]    Exit the chatbot",
            title="Commands",
            border_style="blue",
        )
    )


def show_history(chatbot: GeminiChat) -> None:
    history = chatbot.get_history()

    if not history:
        console.print("[dim]No conversation history.[/dim]")
        return

    console.print(
        Panel(
            f"[bold]Messages:[/bold] {len(history)}",
            title="Conversation History",
            border_style="green",
        )
    )

    for message in history:
        role = message.role

        if not message.parts:
            continue

        for part in message.parts:
            if not part.text:
                continue

            if role == "user":
                console.print(
                    Panel(
                        part.text,
                        title="You",
                        border_style="blue",
                    )
                )

            elif role == "model":
                console.print(
                    Panel(
                        Markdown(part.text),
                        title="Gemini",
                        border_style="green",
                    )
                )


def chat_loop() -> None:
    chatbot = GeminiChat()

    show_welcome()

    while True:
        try:
            user_input = console.input("\n[bold blue]You:[/bold blue] ").strip()

        except KeyboardInterrupt:
            console.print("\n[dim]Goodbye![/dim]")
            break

        except EOFError:
            console.print("\n[dim]Goodbye![/dim]")
            break

        if not user_input:
            continue

        command = user_input.lower()

        if command in {"/exit", "/quit"}:
            console.print("[dim]Goodbye![/dim]")
            break

        if command == "/help":
            show_help()
            continue

        if command == "/clear":
            chatbot.clear_history()
            console.print("[green]Conversation history cleared.[/green]")
            continue

        if command == "/history":
            show_history(chatbot)
            continue

        try:
            with console.status("[bold green]Gemini is thinking...[/bold green]"):
                response = chatbot.send_message(user_input)

            console.print(
                Panel(
                    Markdown(response),
                    title="Gemini",
                    border_style="green",
                )
            )

        except Exception as error:
            console.print(
                Panel(
                    f"[bold red]{error}[/bold red]",
                    title="Error",
                    border_style="red",
                )
            )


if __name__ == "__main__":
    chat_loop()
