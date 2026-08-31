from dataclasses import dataclass

@dataclass(frozen=True)
class AnkiCardCommand:
    deck_name: str
    front: str
    back: str
    image_data: bytes | None = None
    image_filename: str | None = None