from anki.notes import Note
from ..application.dto.AnkiCardCommand import AnkiCardCommand
from ..application.exceptions.card_exceptions import ModelNotFoundError


class AnkiCollectionAdapter:
    def __init__(self, collection):
        self.collection = collection

    def add_card(self, command: AnkiCardCommand) -> int:
    
        # Retrieve the model by name. If the model is not found, raise a ModelNotFoundError.
        model = self.collection.models.by_name(command.model_name)
        
        if model is None:
            raise ModelNotFoundError()

        # Retrieve the deck ID by name.
        deck_id = self.collection.decks.id_for_name(command.deck_name)

        # Create a new note with the specified model.
        note = Note(self.collection, model)
        note["Front"] = command.front
        note["Back"] = command.back

        # Add the note to the collection and save changes.
        note_id = self.collection.add_note(note, deck_id)
        self.collection.save()
        