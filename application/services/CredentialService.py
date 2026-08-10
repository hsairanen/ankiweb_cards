from ...controller.request import SaveApiKeyRequest
from ..credentials.CredentialType import CredentialType
from ..port.CredentialRepository import CredentialRepository

class CredentialService:
    def __init__(self, repository: CredentialRepository):
        self.repository = repository

    def set_api_key(self, request: SaveApiKeyRequest) -> None:
        self.repository.save_api_key(request.credential_type, request.api_key)
    
    def get_api_key(self, credential_type: CredentialType) -> str | None:
        return self.repository.get_api_key(credential_type)

