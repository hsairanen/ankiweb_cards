from abc import ABC, abstractmethod
from ..dto.AIModel import AIModel
from ..dto.VocabCard import VocabCard

class AIAdapter(ABC):

    @abstractmethod
    def run_ai(
        self,
        prompt: str,
        schema: type[VocabCard],
    ) -> VocabCard:
        pass

    @abstractmethod
    def get_available_models(self) -> list[AIModel]:
        pass