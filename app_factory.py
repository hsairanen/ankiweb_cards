import os

from google import genai

from .application.AIService import AIService
from .application.CardService import CardService
from .controller.CardController import CardController
from .infrastructure.GeminiAIAdapter import GeminiPromptAdapter


def build_card_controller() -> CardController:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    
    client = genai.Client(api_key=api_key)
    adapter = GeminiPromptAdapter(client)
    ai_service = AIService(adapter)
    card_service = CardService(ai_service)

    return CardController(card_service)