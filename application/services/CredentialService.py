from ...infrastructure.CredentialAdapter import CredentialAdapter
from ...controller.request import SaveApiKeyRequest

class CredentialService:
    def __init__(self,repository: CredentialAdapter):
        self.adapter = repository

    def set_api_key(self, request: SaveApiKeyRequest) -> None:
        
        self.adapter.save_api_key(request.key_name, request.api_key)
