from google.genai import types
from typing import TypeVar, Type

from ..application.exceptions.ai_exceptions import AIQuotaExceededError, AIServiceError

T = TypeVar("T")

# The adapter class serves as a bridge between the application and the Gemini API.
# It handles the actual HTTP/OpenAI API communication.
# The application code should not directly interact with the Gemini API; 
# instead, it should use this adapter to ensure a clean separation of concerns.
# In other words, the adapter's responsibility is to translate the application's calls into Gemini API calls.
class GeminiPromptAdapter:    
    def __init__(self, client):
        self._client = client
        
   # This method sends a prompt to the Gemini API and returns the parsed response.
   # What could be a better name for this method? It is not just sending a prompt, it is also parsing the response.
    def runAI(self, prompt: str, output_schema: Type[T]) -> T:
        try:
            response = self._client.models.generate_content(
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

        