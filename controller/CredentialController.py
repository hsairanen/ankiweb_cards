from .request import SaveApiKeyRequest
from ..application.services.CredentialService import CredentialService

class CredentialController:
    def __init__(self, credential_service: CredentialService):
        self.credential_service = credential_service
    
    def on_save_clicked(self, request: SaveApiKeyRequest):
        
        return self.credential_service.set_api_key(request=request)