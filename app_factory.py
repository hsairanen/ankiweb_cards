import os
from aqt import mw 

from google import genai

from .infrastructure.AnkiCollectionAdapter import AnkiCollectionAdapter
from .application.services.AIService import AIService
from .application.services.CardService import CardService
from .controller.CardController import CardController
from .infrastructure.GeminiAIAdapter import GeminiPromptAdapter


def build_card_controller() -> CardController:
   
    repository = AnkiCollectionAdapter(collection=mw.col)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)
    gemini_adapter = GeminiPromptAdapter(client)
    ai_service = AIService(gemini_adapter)
    
    card_service = CardService(ai_service, repository)

    return CardController(card_service)