from dataclasses import dataclass

@dataclass(frozen=True)
class AnkiCardCommand:
    deck_name: str
    front: str
    back: str