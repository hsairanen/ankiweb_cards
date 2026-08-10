from dataclasses import dataclass

@dataclass(frozen=True)
class AIModel:
    id: str
    display_name: str