from ..application.dto.AIModel import AIModel
from ..application.services.AIService import AIService

class AIModelController:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    def get_available_models(self) -> list[AIModel]:
        return self.ai_service.get_available_models()
    
