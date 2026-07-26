import os

from google import genai
from google.genai import types

# The adapter class serves as a bridge between the application and the Gemini API.
# It handles the actual HTTP/OpenAI API communication.
# The application code should not directly interact with the Gemini API; 
# instead, it should use this adapter to ensure a clean separation of concerns.
class GeminiPromptAdapter:    
    def __init__(self):
           self._client = None
   
    # This method initializes and returns a client for interacting with the Gemini API.
    def _get_client(self):
        if not self._client:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise RuntimeError("GEMINI_API_KEY is not set")
      
            self._client = genai.Client(api_key=api_key)
        return self._client
   
    
   
        