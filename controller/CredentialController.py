from ..application.services.CredentialService import CredentialService
#from .request.CreateCardRequest import CreateCardRequest

class CredentialController:
    def __init__(self, credential_service: CredentialService):
        self.credential_service = credential_service
