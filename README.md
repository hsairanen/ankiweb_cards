# Anki Cards

A small Python project that generates Anki flashcards from text using Gemini and downloads related images from Pexels.

## Features

- Sends content to Gemini to generate card data
- Creates Anki cards through the Anki API
- Downloads matching images from Pexels
- Stores generated image assets in the local images folder

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the project root.
2. Add your API keys and configuration values, for example:

```env
ANKI_URL=http://localhost:8765
ANKI_DECK=YourDeckName
PEXELS_API_KEY=your_pexels_key
GEMINI_API_KEY=your_gemini_key
```

In the Anki add-on UI, the "Manage API Keys" dialog now includes fields for both the Gemini API key and the image bank API key.

## Run

```bash
python main.py
```

## Anki Add-on UI

In Anki, use the Tools menu item to open the `ankiweb_cards` dockable tab.
It currently provides placeholder input fields for the word, languages, deck name, and model name.
The tab does not run the card-generation workflow yet.

## Project Files

- `main.py` - entry point for the workflow
- `gemini_prompts.py` - Gemini prompt generation
- `gemini_output.py` - response schema for generated card data
- `anki_requests.py` - Anki API integration
- `pexels_requests.py` - image search and download logic
