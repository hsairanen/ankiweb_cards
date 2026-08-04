class AIServiceError(Exception):
    pass

class AIQuotaExceededError(AIServiceError):
    pass