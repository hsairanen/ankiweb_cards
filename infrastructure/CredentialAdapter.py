"""import keyring

SERVICE_NAME = "ankiweb_cards"
KEY_NAME = "api_key"


def get_api_key() -> str | None:
    return keyring.get_password(SERVICE_NAME, KEY_NAME)


def save_api_key(api_key: str) -> None:
    keyring.set_password(SERVICE_NAME, KEY_NAME, api_key)


def delete_api_key() -> None:
    try:
        keyring.delete_password(SERVICE_NAME, KEY_NAME)
    except Exception:
        pass"""

class CredentialAdapter:
    def __init__(self):
        pass