from ..port.ImageAdapter import ImageAdapter

class ImageService:

    def __init__(self, adapter: ImageAdapter):
        self.adapter = adapter

    def fetch_image(self, word: str) -> bytes | None:
        return self.adapter.fetch_image(word)