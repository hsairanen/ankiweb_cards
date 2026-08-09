from pydantic.dataclasses import dataclass

@dataclass(frozen=True)
class SaveApiKeyRequest:
    key_name: str
    api_key: str