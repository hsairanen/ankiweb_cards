from abc import ABC, abstractmethod

class ImageAdapter(ABC):

    @abstractmethod
    def fetch_image(
        self,
        word: str
    ) -> bytes | None:
        pass
