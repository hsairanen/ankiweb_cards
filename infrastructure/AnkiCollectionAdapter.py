from anki.notes import Note
from ..application.dto.AnkiCardCommand import AnkiCardCommand

from ..application.config import AddonConfig

class AnkiCollectionAdapter:
    def __init__(self, collection, addon_config: AddonConfig):
        self.collection = collection
        self.addon_config = addon_config

    def add_card(self, command: AnkiCardCommand):

        model = self.collection.models.by_name(self.addon_config.model_name)

        if model is None:
            model = self.collection.models.new(self.addon_config.model_name)
            self.collection.models.add_field(
                model, self.collection.models.new_field("Front")
            )
            self.collection.models.add_field(
                model, self.collection.models.new_field("Back")
            )
            template = self.collection.models.new_template("Card 1")

            template["qfmt"] = self.addon_config.model_front_template
            template["afmt"] = self.addon_config.model_back_template
            
            self.collection.models.add_template(model, template)
            self.collection.models.add(model)

        deck_id = self.collection.decks.id_for_name(command.deck_name)

        # Create a new note with the specified model.
        note = Note(self.collection, model)
        note["Front"] = command.front
        note["Back"] = command.back

        # Add the note to the collection and save changes.
        self.collection.add_note(note, deck_id)
        self.collection.save()
        