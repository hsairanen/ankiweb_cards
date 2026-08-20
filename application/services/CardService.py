from ...controller.request import CreateCardRequest

from ..dto import AnkiCardCommand
from ..dto.VocabResult import VocabResult
from ..exceptions.ai_exceptions import (
    AIServiceError,
    AIQuotaExceededError,
    MissingApiKeyError
)
from ..dto.AnkiCardCommand import AnkiCardCommand
from ..port.CardRepository import CardRepository

from .AIService import AIService

# This class serves as a service layer for card-related operations.
# CardService is responsible for handling the business logic related to card generation.
class CardService:
    def __init__(self, ai_service: AIService, repository: CardRepository):
        self.ai_service = ai_service
        self.repository = repository

    # This method processes the input word, calls the AI service 
    # to get information about the word, and then creates Anki cards 
    # based on that information.            
    def process_word(self, request: CreateCardRequest) -> VocabResult:

        # Get the AI-generated card information for the given word.
        try:
            card = self.ai_service.run_prompt(request.word, request.model_id)
        except AIQuotaExceededError:
            return VocabResult(
                success=False,
                error="You have reached today's AI limit."
            )
        except AIServiceError:
            return VocabResult(
                success=False,
                error="AI service is currently unavailable. Please try again later."
            )
        except MissingApiKeyError:
            return VocabResult(
                success=False,
                error="AI API key is not configured. Please set it up first."
            )
        
        # Create an Anki card using the information returned by the AI service.
        try:
            to_front = f"{card.definition} ({card.word_trans})"
            to_back = f"{card.word_orig} ({card.example})"
                    
            command = AnkiCardCommand(
                        deck_name=request.deck_name,
                        front=to_front,
                        back=to_back
            )
                    
            self.repository.add_card(command)

        except Exception as e:
            return VocabResult(
                success=False,
                error="Failed to create Anki card."
            )

        return VocabResult(
            success=True,
            card=card
        )