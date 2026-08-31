from aqt import mw
from aqt.qt import (
    QDialog,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
)
from ..controller.request.CreateCardRequest import CreateCardRequest
from ..controller.request.SaveApiKeyRequest import SaveApiKeyRequest
from ..controller.CardController import CardController
from ..controller.CredentialController import CredentialController
from ..controller.AIModelController import AIModelController
from ..application.credentials.CredentialType import CredentialType

from .api_key_dialog import ApiKeyDialog

# This class represents the card tab in the Anki interface. It contains a text input for the user to enter a word and a button to generate cards based on that word.
class CardTab(QWidget):
    def __init__(self, 
                 card_controller: CardController | None, 
                 credential_controller: CredentialController,
                 ai_model_controller: AIModelController):
        super().__init__()
    
        self.card_controller = card_controller
        self.credential_controller = credential_controller
        self.ai_model_controller = ai_model_controller

        # Creates a vertical layout - places components on top of each other
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # ------- MANAGE API KEYS SECTION -------
        
        # Create API button, connect the button click and add the button to the layout
        self.api_button = QPushButton("Manage API Keys")
        self.api_button.clicked.connect(self._handle_api_clicked)
        layout.addWidget(self.api_button)  
        
        # ------- AVAILABLE AI MODELS SECTION -------
        
        model_layout = QVBoxLayout()
        model_layout.setSpacing(4)
        
        model_layout.addWidget(QLabel("Available AI models:"))
        self.model_dropdown = QComboBox()
        self.model_dropdown.addItem("Loading models...")
        self.model_dropdown.setEnabled(False)
        model_layout.addWidget(self.model_dropdown)

        self.model_status_label = QLabel("")
        self.model_status_label.setStyleSheet("color: gray;")
        model_layout.addWidget(self.model_status_label)
        
        layout.addLayout(model_layout)
        
        # ------- CARD GENERATION SECTION -------
        
        deck_layout = QVBoxLayout()
        deck_layout.setSpacing(4)
        
        # Add a label
        deck_layout.addWidget(QLabel("Select deck:"))
                
        # Create a dropdown for deck selection and add it to the layout
        self.deck_dropdown = QComboBox()

        # Fetch all deck names from Anki and populate the dropdown
        self.deck_dropdown.addItems(
            sorted(mw.col.decks.all_names())
        )

        deck_layout.addWidget(self.deck_dropdown)
        
        layout.addLayout(deck_layout)
        
        # --------- WORD ---------------------------------
        
        word_layout = QVBoxLayout()
        word_layout.setSpacing(4)
        
        # Add a label
        word_layout.addWidget(QLabel("Enter word:"))

        # Create text input and add it to the layout
        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText("Type a word...")
        word_layout.addWidget(self.word_input)

        layout.addLayout(word_layout)
        
        # ----------- STATUS ----------------------------- 

        # Create error label, set its style and visibility, 
        # and add it to the layout
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setVisible(False)
        layout.addWidget(self.error_label)
        
        # Create result label, set its style and visibility, 
        # and add it to the layout
        self.result_label = QLabel("")
        self.result_label.setStyleSheet("color: green;")
        self.result_label.setVisible(False)
        layout.addWidget(self.result_label)

        # ------------- GENERATE ---------------------------

        # Create generate button, connect the button click and add the button to the layout
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self._handle_generate_clicked)
        layout.addWidget(self.generate_button)
        
        # Push everything upward instead of spreading it over the whole tab
        layout.addStretch()
        
        self._load_models()

    def _handle_generate_clicked(self) -> None:
        
        selected_deck = self.deck_dropdown.currentText()
        request = CreateCardRequest(
            deck_name=selected_deck,
            word=self.word_input.text(),
            model_id=self.model_dropdown.currentData()
        )
        
        result = self.card_controller.on_generate_clicked(request)
        
        if not result.success:
            self.error_label.setText(result.error)
            self.error_label.setVisible(True)
            return

        self.error_label.setVisible(False)

        self.result_label.setText(
            f"A card generated successfully for "
            f"the word '{result.card.word_trans}'!"
        )
        self.result_label.setVisible(True)
        

    def _handle_api_clicked(self) -> None:
        dialog = ApiKeyDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            gemini_api_key = dialog.get_api_key()
            if gemini_api_key:
                self.credential_controller.on_save_clicked(
                    SaveApiKeyRequest(
                        credential_type=CredentialType.GEMINI,
                        api_key=gemini_api_key,
                    )
                )

            image_bank_api_key = dialog.get_image_bank_api_key()
            if image_bank_api_key:
                self.credential_controller.on_save_clicked(
                    SaveApiKeyRequest(
                        credential_type=CredentialType.PEXELS,
                        api_key=image_bank_api_key,
                    )
                )

            self._load_models()
    
    def _load_models(self) -> None:
        models = self.ai_model_controller.get_available_models()

        self.model_dropdown.clear()

        for model in models:
            self.model_dropdown.addItem(
                model.display_name,
                model.id,
            )

        self.model_dropdown.setEnabled(True)