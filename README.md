# ankiweb_cards

An Anki add-on that generates vocabulary cards from a word using Gemini and can attach a matching image from Pexels.

## Features

- Adds a dockable panel to Anki
- Lets the user select an available Gemini model
- Lets the user choose a target deck from the current Anki collection
- Generates a card from a word using the AI service
- Saves Gemini and Pexels API keys through the Windows Credential Manager via `keyring`
- Downloads a related image from Pexels when available

## Requirements

- Anki desktop
- Python dependencies from `requirements.txt`
- A valid Gemini API key
- A valid Pexels API key

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

1. Place this project in Anki's add-ons folder or install it as an add-on.
2. Start Anki.
3. Open the Tools menu and select `Create AI cards`.
4. Click `Manage API Keys` and save both the Gemini key and the Pexels key.
5. Select a deck and AI model, enter a word, and click `Generate`.

## How it works

- The add-on is initialized from `__init__.py` and `menu_setup.py`.
- `app_factory.py` wires the services, controllers, and adapters together.
- `CardTab` provides the dockable Anki UI.
- `GeminiAIAdapter` calls the Gemini API to generate vocabulary content.
- `PexelImageAdapter` calls the Pexels API for related images.
- `CredentialAdapter` stores credentials in the Windows Credential Manager using `keyring`.

## Project structure

- `ui/` - Anki UI panels and dialogs
- `controller/` - request handling and UI controller logic
- `application/` - services, ports, DTOs, and config
- `infrastructure/` - API adapters for Gemini, Pexels, Anki, and credentials
- `__init__.py` - Anki add-on entry point
- `app_factory.py` - dependency wiring for the add-on
