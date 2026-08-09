import keyring

class CredentialAdapter:
    SERVICE_NAME = "ankiweb_cards"    
    
    def __init__(self):
        pass
    
    def get_api_key(self, key_name: str) -> str | None:
        return keyring.get_password(self.SERVICE_NAME, key_name)

    def save_api_key(self, key_name: str, api_key: str) -> None:
        keyring.set_password(self.SERVICE_NAME, key_name, api_key)

    def delete_api_key(self, key_name: str) -> None:
        try:
            keyring.delete_password(self.SERVICE_NAME, key_name)
        except Exception:
            pass

