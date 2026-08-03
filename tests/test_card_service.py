from unittest.mock import Mock

from application.CardService import CardService

# This test checks that the process_word method of CardService 
# correctly delegates to the AIService's method 
# and returns the expected response.
def test_process_word_delegates_to_ai_service_and_returns_response():
    ai_service = Mock()
    # Set up the mock to return a specific value when write_prompt is called
    ai_service.write_prompt.return_value = {"word": "hola"}
    
    # Create an instance of CardService with the mocked AIService
    service = CardService(ai_service)

    # Call the method under test
    result = service.process_word("hola")

    # Assert that the AIService's write_prompt method was called with the correct argument
    ai_service.write_prompt.assert_called_once_with("hola")
    assert result == {"word": "hola"}