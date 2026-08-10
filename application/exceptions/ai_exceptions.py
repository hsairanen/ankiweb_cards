class AIServiceError(Exception):
    pass

class AIQuotaExceededError(AIServiceError):
    pass

class MissingApiKeyError(Exception):
    pass