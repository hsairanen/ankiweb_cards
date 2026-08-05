from ..dto.VocabCard import VocabCard

# This class serves as a service layer for AI-related operations. 
# AIService is responsible for prompt engineering and AI-related logic

class AIService:
    SCHEMA = VocabCard
    
    def __init__(self, adapter):
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
  
        return self.adapter.runAI(prompt, self.SCHEMA)
    
