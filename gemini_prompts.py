# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:18:26 2026

@author: heidi
"""

import os
from google import genai
from google.genai import types
from gemini_output import VocabCard


def _get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    return genai.Client(api_key=api_key)

def generate_card_data(word: str, source_language: str ="Spanish", target_language: str="English"):
    prompt = f"""
    Identify the most common meaning of the word in {source_language} 
    and translate it into {target_language}. Explain the word clearly and learner-friendly
    way in {source_language} and give an example sentence in {source_language}.
    
    Word: {word}
    Source language: {source_language}
    Target language: {target_language}
    """

    client = _get_client()

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=VocabCard,
            temperature=0.2,
        ),
    )

    return response.parsed

