# Gemini Chat Bot

A simple terminal-based AI chatbot built with **Python**, **Google Gemini API**, **uv**, and **Rich**.

The project is part of the `py-hobby` repository and is designed as a practical project for learning how to integrate Google's Gemini API into a Python application.

## Features

- 🤖 Google Gemini API integration
- 💬 Multi-turn conversations
- 🧠 Conversation history during the current session
- 🎨 Rich terminal interface
- 🔐 API key stored securely in `.env`
- ⚡ Fast dependency management with `uv`
- 🧹 Clear conversation history
- 📜 View conversation history
- ❓ Built-in help command
- 🚪 Exit command

## Tech Stack

- **Python 3.14+**
- **Google GenAI SDK**
- **uv**
- **python-dotenv**
- **Rich**

## Project Structure

```text
gemini-chat-bot/
│
├── src/
│   └── gemini_chat_bot/
│       ├── __init__.py
│       ├── config.py
│       ├── gemini.py
│       └── main.py
│
├── .env
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock
```

### File Responsibilities

| File             | Purpose                                                   |
| ---------------- | --------------------------------------------------------- |
| `config.py`      | Loads environment variables and application configuration |
| `gemini.py`      | Handles communication with the Gemini API                 |
| `main.py`        | Handles the terminal interface and user interaction       |
| `.env`           | Stores the Gemini API key                                 |
| `.env.example`   | Template for environment variables                        |
| `pyproject.toml` | Project metadata and dependencies                         |
| `uv.lock`        | Locks dependency versions                                 |

## Requirements

Before running the project, make sure you have:

- Python 3.14+
- `uv`
- A Google Gemini API key

### Regional Availability / VPN

If the Gemini API returns an error indicating that the service is **not available in your country or region**, the issue may be related to regional availability rather than your code.

In that case, connect to a **VPN server in a country where the Gemini API is available**, then run the application again.

> **Note:** A VPN does not fix an invalid API key, incorrect configuration, quota limits, or other API errors. Check the actual error message first.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/naji-basir/py-hobby.git
```

Then enter the project:

```bash
cd py-hobby/projects/gemini-chat-bot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

You can use `.env.example` as a template:

```env
GEMINI_API_KEY=
```

**Never commit your `.env` file or expose your API key publicly.**

## Running the Application

Run the chatbot with:

```bash
uv run gemini-chat-bot
```

Alternatively, you can run the Python module directly:

```bash
uv run python -m gemini_chat_bot.main
```

## Available Commands

Inside the chatbot:

| Command    | Description                    |
| ---------- | ------------------------------ |
| `/help`    | Display available commands     |
| `/clear`   | Clear the current conversation |
| `/history` | Display conversation history   |
| `/exit`    | Exit the chatbot               |
| `/quit`    | Exit the chatbot               |

## Example

```text
╭────────────────────────────────╮
│         Gemini Chatbot         │
│    Powered by Google Gemini    │
│                                │
│ Type /help to see commands.    │
╰────────────────────────────────╯

You: What is dependency injection?

Gemini:
Dependency injection is a design pattern where...

You: Give me a Python example.

Gemini:
Here's a simple example...

You: /history

Conversation History
Messages: 4
```

The chatbot maintains context throughout the current session.

For example:

```text
You: My name is Naji.

Gemini: Nice to meet you, Naji!

You: What is my name?

Gemini: Your name is Naji.
```

## Environment Variables

The application currently requires:

```env
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded using `python-dotenv`.

## Conversation History

Conversation history is maintained by the Gemini chat session.

The history exists only while the application is running.

If you exit the application and start it again, the previous conversation is not automatically restored.

Persistent conversation storage can be added in a future version using SQLite or another database.

## Development

Install or update dependencies:

```bash
uv sync
```

Add a dependency:

```bash
uv add package-name
```

Remove a dependency:

```bash
uv remove package-name
```

Run the application:

```bash
uv run gemini-chat-bot
```

## Roadmap

### Version 1

- [x] Gemini API integration
- [x] Terminal chatbot
- [x] Conversation history
- [x] Rich terminal UI
- [x] Environment configuration
- [x] Basic commands

### Version 2

- [x] Streaming Gemini responses
- [ ] Improved error handling
- [ ] Token usage information
- [ ] Configurable Gemini model
- [ ] Better terminal UX

### Version 3

- [ ] Persistent conversation history
- [ ] SQLite database
- [ ] Multiple conversations
- [ ] Conversation titles
- [ ] System prompts

### Version 4

- [ ] File upload
- [ ] PDF/document conversations
- [ ] Image understanding
- [ ] More Gemini capabilities

### Version 5

- [ ] FastAPI backend
- [ ] Web interface
- [ ] User authentication
- [ ] Web-based conversation history

## Security

Never commit your Gemini API key.

Make sure `.gitignore` contains:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If an API key is accidentally pushed to GitHub, **revoke and regenerate the key immediately**. Removing it from the latest commit is not sufficient because the key may remain in Git history.

## License

This project is for educational and hobby purposes.
