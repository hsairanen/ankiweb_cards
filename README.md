# ankiweb_cards
This python tool helps you create cards to Anki Web application. 

**Requirements**
1) You need a API key to Google Gemini and a API key to Pexel (a free image bank).
Store these API keys in an .env file for the app.
2) You also need a Anki Connector installed in you Anki Desktop.
3) When you run this app, you need to have Anki Desktop open/running.
4) You can create a template for cards in Anki Desktop. Mine is called "AI Vocabulary Typing" and it requires the input of the card includes a text field. 

**What is this app about?**
You give the code a Spanish word. The app uses Google Gemini AI to find its translation, description in Spanish and an example sentence in Spanish. 

After the Gemini, the app calls Pexel API and fetches an image using the English translation. Basically, the app could be fetch several images but since it does not have any selection logic for images, it is good to search only one.

Finally, the app calls Anki Desktop and creates a card using the information from Gemini and Pexel. 
