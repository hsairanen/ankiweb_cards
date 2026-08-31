from aqt import mw 

from .ui.card_tab import CardTab

from .controller.CredentialController import CredentialController
from .application.services.CredentialService import CredentialService
from .infrastructure.CredentialAdapter import CredentialAdapter

from .application.config import load_addon_config
from .application.services.AIService import AIService
from .application.services.ImageService import ImageService
from .application.services.CardService import CardService
from .controller.CardController import CardController
from .infrastructure.AnkiCollectionAdapter import AnkiCollectionAdapter
from .infrastructure.GeminiAIAdapter import GeminiPromptAdapter
from .infrastructure.PexelImageAdapter import PexelImageAdapter

from .controller.AIModelController import AIModelController

# This function is used to wire things together and build the card tab for the UI.
def build_card_tab() -> CardTab:
    
    credential_repository = CredentialAdapter()
    credential_service = CredentialService(credential_repository)
    credential_controller = CredentialController(credential_service)
    
    config = load_addon_config()
    anki_repository = AnkiCollectionAdapter(collection=mw.col, addon_config=config)
    
    gemini_adapter = GeminiPromptAdapter(credential_repository=credential_repository)
    ai_service = AIService(gemini_adapter)
    
    image_adapter = PexelImageAdapter(credential_repository=credential_repository)
    image_service = ImageService(image_adapter)
    
    card_service = CardService(ai_service, image_service, anki_repository)
    card_controller = CardController(card_service)
    
    ai_model_controller = AIModelController(ai_service)
    
    return CardTab(card_controller=card_controller,
                   credential_controller=credential_controller,
                   ai_model_controller=ai_model_controller)