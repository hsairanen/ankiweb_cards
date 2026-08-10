import keyring
from ..application.credentials.CredentialType import CredentialType

class CredentialAdapter:
    SERVICE_NAME = "ankiweb_cards"    
    
    def __init__(self):
        pass
    
    def get_api_key(self, api_key_name: CredentialType) -> str | None:
        # Return None if the API key is not found
        try:
            return keyring.get_password(self.SERVICE_NAME, api_key_name.value)
        except Exception:
            return None

    def save_api_key(self, api_key_name: CredentialType, api_key: str) -> None:
        keyring.set_password(self.SERVICE_NAME, api_key_name.value, api_key)

    def delete_api_key(self, api_key_name: CredentialType) -> None:
        try:
            keyring.delete_password(self.SERVICE_NAME, api_key_name.value)
        except Exception:
            pass

