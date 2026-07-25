import json
import os

from aqt import mw
from aqt.gui_hooks import main_window_did_init
from aqt.qt import QAction
from aqt.utils import showInfo


def setup() -> None:
    main_window_did_init.append(_add_test_action)


def _add_test_action() -> None:
    action = QAction("Generate ankiweb_cards card", mw)
    action.triggered.connect(_generate_card)
    mw.form.menuTools.addAction(action)


def _load_config() -> dict:
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

    with open(config_path, "r", encoding="utf-8") as config_file:
        return json.load(config_file)


def _generate_card() -> None:
    try:
        from ..main import create_card_from_word

        config = _load_config()
        create_card_from_word(
            config["word"],
            deck_name=config["deck_name"],
            model_name=config["model_name"],
            source_language=config.get("source_language", "Spanish"),
            target_language=config.get("target_language", "English"),
        )
        showInfo("ankiweb_cards card generated successfully.")
    except Exception as error:
        showInfo(f"ankiweb_cards failed: {error}")