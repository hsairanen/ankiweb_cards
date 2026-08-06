from __future__ import annotations

import sys
import types

from ..application.dto.AnkiCardCommand import AnkiCardCommand


anki_module = types.ModuleType("anki")
notes_module = types.ModuleType("anki.notes")


class FakeNote(dict):
    def __init__(self, collection, model):
        super().__init__()
        self.collection = collection
        self.model = model


notes_module.Note = FakeNote
anki_module.notes = notes_module
sys.modules.setdefault("anki", anki_module)
sys.modules.setdefault("anki.notes", notes_module)

from ..infrastructure.AnkiCollectionAdapter import AnkiCollectionAdapter


class FakeModels:
    def __init__(self):
        self.models = {}
        self.added_fields = []
        self.added_templates = []
        self.added_models = []

    def by_name(self, name):
        return self.models.get(name)

    def new(self, name):
        return {"name": name, "flds": [], "tmpls": [], "id": 0}

    def new_field(self, name):
        return {"name": name, "ord": None}

    def add_field(self, model, field):
        model["flds"].append(field)
        self.added_fields.append((model["name"], field["name"]))

    def new_template(self, name):
        return {"name": name, "qfmt": "", "afmt": "", "ord": None}

    def add_template(self, model, template):
        model["tmpls"].append(template)
        self.added_templates.append((model["name"], template["name"]))

    def add(self, model):
        model["id"] = 1
        self.models[model["name"]] = model
        self.added_models.append(model["name"])


class FakeDecks:
    def id_for_name(self, name):
        return 42


class FakeCollection:
    def __init__(self):
        self.models = FakeModels()
        self.decks = FakeDecks()
        self.added_notes = []
        self.saved = False

    def add_note(self, note, deck_id):
        self.added_notes.append((note, deck_id))
        return 99

    def save(self):
        self.saved = True


def test_add_card_creates_missing_model_before_adding_note():
    collection = FakeCollection()
    adapter = AnkiCollectionAdapter(collection)

    command = AnkiCardCommand(
        deck_name="Default",
        model_name="AI Vocabulary Typing",
        front="front text",
        back="back text",
    )

    note_id = adapter.add_card(command)

    assert note_id == 99
    assert collection.models.added_models == ["AI Vocabulary Typing"]
    assert collection.models.added_fields == [
        ("AI Vocabulary Typing", "Front"),
        ("AI Vocabulary Typing", "Back"),
    ]
    assert collection.models.added_templates == [("AI Vocabulary Typing", "Card 1")]
    note, deck_id = collection.added_notes[0]
    assert deck_id == 42
    assert note["Front"] == "front text"
    assert note["Back"] == "back text"
    assert collection.saved is True