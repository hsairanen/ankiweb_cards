from pydantic.dataclasses import dataclass

from ...application.credentials.CredentialType import CredentialType

@dataclass(frozen=True)
class SaveApiKeyRequest:
    credential_type: CredentialType
    api_key: str