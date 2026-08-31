import requests

from ..application.credentials.CredentialType import CredentialType
from ..application.port.CredentialRepository import CredentialRepository
from ..application.exceptions.image_exceptions import ImageServiceError

class PexelImageAdapter:    
    def __init__(self, credential_repository: CredentialRepository):
        self._credential_repository = credential_repository
        
    def fetch_image(self, word: str) -> bytes:
        api_key = self._credential_repository.get_api_key(CredentialType.PEXELS)
        
        # Return None if the API key is not available
        if not api_key:
            return None  
    
        try:        
            url = "https://api.pexels.com/v1/search"

            headers = {
                "Authorization": api_key
            }

            params = {
                "query": word,
                "per_page": 1,
                "orientation": "landscape"
            }

            response = requests.get(url, headers=headers, params=params, timeout=15)
            response.raise_for_status()

            data = response.json()
            
            if data is None:
                raise ValueError("No response was returned by the image bank.")

            photos = data.get("photos", [])
                
            image_url = photos[0]["src"]["large"]

            image_response = requests.get(
                image_url,
                timeout=15,
            )

            image_response.raise_for_status()

            return image_response.content

        except Exception as e:
            raise ImageServiceError("An error occurred while fetching the image.") from e
