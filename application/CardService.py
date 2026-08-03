from .AIService import AIService

# This class serves as a service layer for card-related operations.
# CardService is responsible for handling the business logic related to card generation.
class CardService:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    # This method processes the input word, calls the AI service 
    # to get information about the word, and then creates Anki cards 
    # based on that information.            
    def process_word(self, word: str):

        response = 'testing'
        # Call AI
        #response = self.ai_service.get_word_info(word)
        # Parse response
        # Create Anki cards
        return response