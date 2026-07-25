# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:19:46 2026

@author: heidi
"""

from anki_requests import add_anki_card
from gemini_prompts import generate_card_data
from pexels_requests import search_and_download_image

def create_card_from_word(
    word: str,
    deck_name: str,
    model_name: str,
    source_language: str = "Spanish",
    target_language: str = "English",
) -> None:
    
    card = generate_card_data(
        word,
        source_language=source_language,
        target_language=target_language,
    )

    output_paths = search_and_download_image(query=card.word_trans, count=1)

    to_front = f"{card.definition} ({card.word_trans})"
    to_back = f"{card.word_orig} ({card.example})"

    add_anki_card(
        deck_name,
        model_name,
        to_front,
        to_back,
        image_path=output_paths[0] if output_paths else None,
    )


if __name__ == "__main__":
    create_card_from_word(
        "cirujano",
        deck_name="Español::Clase 2026",
        model_name="AI Vocabulary Typing",
        source_language="Spanish",
        target_language="English"
    )



