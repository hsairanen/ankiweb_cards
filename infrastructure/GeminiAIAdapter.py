from google import genai
from google.genai import types

# The adapter class serves as a bridge between the application and the Gemini API.
# It handles the actual HTTP/OpenAI API communication.
# The application code should not directly interact with the Gemini API; 
# instead, it should use this adapter to ensure a clean separation of concerns.
# In other words, the adapter's responsibility is to translate the application's calls into Gemini API calls.
class GeminiPromptAdapter:    
    def __init__(self, client):
        self._client = client
        
   # This method sends a prompt to the Gemini API and returns the parsed response.
    def send_prompt(self, prompt: str, output_schema):
        response = self._client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=output_schema,
            temperature=0.2)
        )

        return response.parsed

        