from unittest.mock import Mock

from application.CardService import CardService


class TestCardService:

    def test_process_word_delegates_to_ai_service_and_returns_response(self):
        ai_service = Mock()

        # Simulate an arbitrary parsed Pydantic response object
        response = Mock()
        ai_service.run_prompt.return_value = response

        service = CardService(ai_service)

        result = service.process_word("hola")

        ai_service.run_prompt.assert_called_once_with("hola")
        assert result is response