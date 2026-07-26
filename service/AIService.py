import os
from google import genai

class AIService:
    def __init__(self):
        self._client = None

    def _get_client(self):
        if not self._client:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise RuntimeError("GEMINI_API_KEY is not set")
   
            self._client = genai.Client(api_key=api_key)
        return self._client
