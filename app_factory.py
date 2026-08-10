import os
from aqt import mw 

from google import genai

from .ui.card_tab import CardTab

from .controller.CredentialController import CredentialController
from .application.services.CredentialService import CredentialService
from .application.port.CredentialRepository import CredentialRepository
from .infrastructure.CredentialAdapter import CredentialAdapter

from .application.config import load_addon_config
from .application.services.AIService import AIService
from .application.services.CardService import CardService
from .controller.CardController import CardController
from .infrastructure.AnkiCollectionAdapter import AnkiCollectionAdapter
from .infrastructure.GeminiAIAdapter import GeminiPromptAdapter

def build_card_controller(credential_repository: CredentialRepository) -> CardController:
   
    config = load_addon_config()
    anki_repository = AnkiCollectionAdapter(collection=mw.col, addon_config=config)
    
    gemini_adapter = GeminiPromptAdapter(credential_repository=credential_repository)
    ai_service = AIService(gemini_adapter)
    
    card_service = CardService(ai_service, anki_repository)

    return CardController(card_service)


# This function is used to wire things together and build the card tab for the UI.
def build_card_tab() -> CardTab:
    
    credentialRepository = CredentialAdapter()
    credential_service = CredentialService(credentialRepository)
    credential_controller = CredentialController(credential_service)
    
    card_controller = build_card_controller(credential_repository=credentialRepository)
    
    return CardTab(card_controller=card_controller,
                   credential_controller=credential_controller)