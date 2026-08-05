from abc import ABC, abstractmethod

from ..dto.AnkiCardCommand import AnkiCardCommand


class CardRepository(ABC):

    @abstractmethod
    def add_card(self, command: AnkiCardCommand) -> int:
        pass