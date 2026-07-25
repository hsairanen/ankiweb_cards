# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:19:46 2026

@author: heidi
"""

import os

os.chdir("C:/Users/heidi/Documents/ankicards")

from anki_requests import add_anki_card
from gemini_prompts import generate_card_data
from pexels_requests import search_and_download_image

DECK_NAME = "Español::Clase 2026"
MODEL_NAME = "AI Vocabulary Typing"


# Run AI to get translations and description of the given word
card = generate_card_data("enfatizar", 
                          source_language="Spanish",
                          target_language="English")


# Search and download image, return the location where they were stored
output_paths = search_and_download_image(query=card.word_trans,count=1)

# Get front and back text from the card
to_front = f"{card.definition} ({card.word_trans})" 
to_back = f"{card.word_orig} ({card.example})" 

# Create Anki card 
add_anki_card(DECK_NAME, 
              MODEL_NAME,
              to_front,
              to_back,
              image_path=output_paths[0])



