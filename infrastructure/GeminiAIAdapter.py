from google import genai
from google.genai import types
from typing import TypeVar, Type

from ..application.credentials.CredentialType import CredentialType
from ..application.port import CredentialRepository
from ..application.exceptions.ai_exceptions import AIQuotaExceededError, AIServiceError, MissingApiKeyError
from ..application.dto.AIModel import AIModel

T = TypeVar("T")

# The adapter class serves as a bridge between the application and the Gemini API.
class GeminiPromptAdapter:    
    def __init__(self, credential_repository: CredentialRepository):
        self._credential_repository = credential_repository
        
    def run_ai(self, prompt: str, output_schema: Type[T]) -> T:
        api_key = self._credential_repository.get_api_key(CredentialType.GEMINI)
            
        if not api_key:
            raise MissingApiKeyError()
    
        try:        
            client = genai.Client(api_key=api_key)
            
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=output_schema,
                temperature=0.2)
            )
            
            if response.parsed is None:
                raise ValueError("No response was returned by the AI.")

            return response.parsed
        except Exception as e:
            if "Quota exceeded" in str(e):
                raise AIQuotaExceededError() from e

            raise AIServiceError() from e
    
    def get_available_models(self) -> list[AIModel]:
        api_key = self._credential_repository.get_api_key(CredentialType.GEMINI)
            
        if not api_key:
            raise MissingApiKeyError()
        
        try:
            client = genai.Client(api_key=api_key)
            models = client.models.list()
            return [AIModel(id=model.name, display_name=model.display_name) for model in models
                    if "generateContent" in model.supported_actions]
        except Exception as e:
            if "Quota exceeded" in str(e):
                raise AIQuotaExceededError() from e

            raise AIServiceError() from e

        