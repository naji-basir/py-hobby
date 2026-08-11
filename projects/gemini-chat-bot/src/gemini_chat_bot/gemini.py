from google import genai
from .config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiChat:
    def __init__(self) -> None:
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.chat = self.client.chats.create(model=GEMINI_MODEL)

    def send_message(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text

    def get_history(self):
        return self.chat.get_history()

    def clear_history(self) -> None:
        self.chat = self.client.chats.create(model=GEMINI_MODEL)
