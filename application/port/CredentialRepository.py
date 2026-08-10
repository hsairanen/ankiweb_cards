from abc import ABC, abstractmethod

from ..credentials.CredentialType import CredentialType

class CredentialRepository(ABC):

    @abstractmethod
    def get_api_key(self, credential_type: CredentialType) -> str | None:
        pass

    @abstractmethod
    def save_api_key(self, credential_type: CredentialType, api_key: str) -> None:
        pass

    @abstractmethod
    def delete_api_key(self, credential_type: CredentialType) -> None:
        pass