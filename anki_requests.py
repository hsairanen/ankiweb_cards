# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:09:11 2026

@author: heidi
"""

import requests
import os

ANKI_CONNECT_URL = "http://localhost:8765"

# Action is the anki command you want to run (e.g. "addNote", "findNote") 
# Params is additional information (e.g. deck name, model name, fields)
# This functions is a helper for sending a request to Anki as a json object

def anki_request(action, params=None):
    response = requests.post(
        ANKI_CONNECT_URL,
        json={
            "action": action,
            "version": 6,
            "params": params or {}
        }
    )
    data = response.json()
    
    if data.get("error"):
        raise Exception(f"AnkiConnect error: {data['error']}")
    
    return data['result'] 


def add_anki_card(deck_name, model_name, front, back, image_path=None, tags=None):
    note = {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            "Front": front,
            "Back": back
        },
        "tags": tags or []
    }

    if image_path:
        image_path = os.path.abspath(image_path)
        image_filename = os.path.basename(image_path)

        # Image first, text below
        note["fields"]["Front"] = f'<img src="{image_filename}"><br>{front}'

        note["picture"] = [
            {
                "path": image_path,
                "filename": image_filename,
                "fields": []
            }
        ]

    return anki_request("addNote", {
        "note": note
    })
    
    
    
    
