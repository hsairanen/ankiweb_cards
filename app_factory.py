import os
from aqt import mw 

from google import genai

from .controller.CredentialController import CredentialController
from .application.services.CredentialService import CredentialService
from .infrastructure.CredentialAdapter import CredentialAdapter

from .application.config import load_addon_config
from .application.services.AIService import AIService
from .application.services.CardService import CardService
from .controller.CardController import CardController
from .infrastructure.AnkiCollectionAdapter import AnkiCollectionAdapter
from .infrastructure.GeminiAIAdapter import GeminiPromptAdapter

def build_credential_controller() -> CredentialController:
    repository = CredentialAdapter()
    #credential_service = CredentialService(repository) # Not build yet
    credential_service = CredentialService()
    return CredentialController(credential_service)


def build_card_controller(api_key: str) -> CardController:
   
    config = load_addon_config()
    repository = AnkiCollectionAdapter(collection=mw.col, addon_config=config)
    
    client = genai.Client(api_key=api_key)
    gemini_adapter = GeminiPromptAdapter(client)
    ai_service = AIService(gemini_adapter)
    
    card_service = CardService(ai_service, repository)

    return CardController(card_service)

def build_card_controller_if_configured(credential_controller: CredentialController) -> CardController | None:
    
    #api_key = credential_controller.get_credential("GEMINI_API_KEY")
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return None
    
    return build_card_controller(api_key)