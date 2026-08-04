from .dto import VocabResult
from .dto.VocabCard import VocabCard
from .exceptions.ai_exceptions import (
    AIServiceError,
    AIQuotaExceededError,
)
from .AIService import AIService

# This class serves as a service layer for card-related operations.
# CardService is responsible for handling the business logic related to card generation.
class CardService:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    # This method processes the input word, calls the AI service 
    # to get information about the word, and then creates Anki cards 
    # based on that information.            
    def process_word(self, word: str) -> VocabResult:

        try:
            card = self.ai_service.run_prompt(word)
            
            return VocabResult(
                            success=True,
                            card=card
                        )
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