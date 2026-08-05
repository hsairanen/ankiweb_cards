from pydantic.dataclasses import dataclass

@dataclass(frozen=True)
class CreateCardRequest:
    deck_name: str
    word: str