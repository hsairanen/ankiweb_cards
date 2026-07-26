#from google import genai
from .AIService import AIService

# This class serves as a service layer for card-related operations.
# CardService is responsible for handling the business logic related to card generation.
class CardService:
    def __init__(self):
        pass
        #self.ai_service = AIService()
        
    #api_key = os.getenv("GEMINI_API_KEY")
    #client = genai.Client(api_key=api_key)
    #adapter = GeminiPromptAdapter(client)
    #ai_service = AIService(adapter)
    #card_service = CardService(ai_service)

    def process_word(self, word: str):
        response = 'testing'
        # Call AI
        #response = self.ai_service.get_word_info(word)
        # Parse response
        # Create Anki cards
        return response