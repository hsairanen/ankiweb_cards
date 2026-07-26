from pydantic import BaseModel, Field

class VocabCard(BaseModel):
    word_orig: str = Field(description="The original word exactly as the user entered it. But include indefinite articles if missing when the word is noun.")
    word_trans: str = Field(description="The simplest and most common translation of the word. Include indefinite articles if a noun.")
    definition: str = Field(description="A short, learner-friendly explanation of the word's meaning in the original language.")
    example: str = Field(description="One natural sentence using the original word.")    
    
    
