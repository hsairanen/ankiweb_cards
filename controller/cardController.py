from ..service.cardService import cardService


class cardController:
    def __init__(self):
        self.card_service = cardService()

    def create_cards(self, word: str) -> None:
        self.card_service.create_cards(word)