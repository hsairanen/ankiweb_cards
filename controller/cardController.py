from ..service.CardService import CardService

class CardController:
    def __init__(self):
        self.card_service = CardService()

    # This function is called when the "Generate" button is clicked. 
    # It retrieves the word from the input field, validates it, and then calls the card service 
    # to create cards based on that word.        
    def on_generate_clicked(self, word: str) -> None:
        # Check that the word contains only letters and spaces
        if not word.replace(" ", "").isalpha():
            raise ValueError("Please enter a word containing only letters and spaces.")

        response = self.card_service.process_word(word)
        if isinstance(response, str):
           return response

        return None 