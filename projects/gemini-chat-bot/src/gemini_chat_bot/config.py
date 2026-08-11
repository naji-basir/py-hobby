import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. " "Create a .env file and add your Gemini API key."
    )

GEMINI_MODEL = "gemini-3.6-flash"
