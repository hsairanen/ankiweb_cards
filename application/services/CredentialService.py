"""from aqt import mw

from ...infrastructure.credentials import (
    get_api_key,
    save_api_key,
)
from ..ui.api_key_dialog import ApiKeyDialog

class CredentialService:
    def __init__(self):
        self.api_key = None
        
    def get_or_request_api_key(self) -> str | None:
        api_key = get_api_key()

        if api_key:
            return api_key

        dialog = ApiKeyDialog(mw)

        if not dialog.exec():
            return None

        api_key = dialog.api_key

        if not api_key:
            return None

        save_api_key(api_key)

        return api_key"""


class CredentialService:
    def __init__(self):
        pass
