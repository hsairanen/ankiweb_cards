from ..application.dto.VocabResult import VocabResult
from ..application.services.CardService import CardService
from .request.CreateCardRequest import CreateCardRequest

class CardController:
    def __init__(self, card_service: CardService):
        self.card_service = card_service

    # This function is called when the "Generate" button is clicked. 
    # It retrieves the word from the input field, validates it, and then calls the card service 
    # to create cards based on that word.        
    def on_generate_clicked(self, request: CreateCardRequest) -> VocabResult:

        if not request.word.replace(" ", "").isalpha():
            return VocabResult(
                success=False,
                error="Please enter a word containing only letters and spaces."
            )

        return self.card_service.process_word(request)
    