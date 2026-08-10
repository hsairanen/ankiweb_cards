from ..port.AIAdapter import AIAdapter
from ..dto.VocabCard import VocabCard
from ..dto.AIModel import AIModel

# This class serves as a service layer for AI-related operations. 
# AIService is responsible for prompt engineering and AI-related logic
class AIService:
    SCHEMA = VocabCard
    
    def __init__(self, adapter: AIAdapter):
        self.adapter = adapter
    
    def run_prompt(self, word: str, source_language: str = "Spanish", target_language: str = "English") -> VocabCard:        
        prompt = f"""
        Identify the most common meaning of the word in {source_language} 
        and translate it into {target_language}. Explain the word clearly and learner-friendly
        way in {source_language} and give an example sentence in {source_language}.
        
        Word: {word}
        Source language: {source_language}
        Target language: {target_language}
        """
  
        return self.adapter.run_ai(prompt, self.SCHEMA)
    
    def get_available_models(self) -> list[AIModel]:
        # Here we could add some filtering or processing logic if needed, but for now, we simply return the models from the adapter.
        return self.adapter.get_available_models()
    
