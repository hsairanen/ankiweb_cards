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
from ..application.credentials.CredentialType import CredentialType

from .api_key_dialog import ApiKeyDialog

# This class represents the card tab in the Anki interface. It contains a text input for the user to enter a word and a button to generate cards based on that word.
class CardTab(QWidget):
    def __init__(self, 
                 card_controller: CardController | None, 
                 credential_controller: CredentialController):
        super().__init__()
    
        self.card_controller = card_controller
        self.credential_controller = credential_controller

        # Creates a vertical layout - places components on top of each other
        layout = QVBoxLayout(self)
        
        # Create API button, connect the button click and add the button to the layout
        self.api_button = QPushButton("Manage API Keys")
        self.api_button.clicked.connect(self._handle_api_clicked)
        layout.addWidget(self.api_button)  
        
        # Add a label
        layout.addWidget(QLabel("Select deck:"))
                
        # Create a dropdown for deck selection and add it to the layout
        self.deck_dropdown = QComboBox()

        # Fetch all deck names from Anki and populate the dropdown
        self.deck_dropdown.addItems(
            sorted(mw.col.decks.all_names())
        )

        layout.addWidget(self.deck_dropdown)
        
        # Add a label
        layout.addWidget(QLabel("Enter word:"))

        # Create text input and add it to the layout
        self.word_input = QLineEdit()
        self.word_input.setPlaceholderText("Type a word...")
        layout.addWidget(self.word_input)

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

        # Create generate button, connect the button click and add the button to the layout
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self._handle_generate_clicked)
        layout.addWidget(self.generate_button)

    def _handle_generate_clicked(self) -> None:
        
        selected_deck = self.deck_dropdown.currentText()
        request = CreateCardRequest(
            deck_name=selected_deck,
            word=self.word_input.text()
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
            api_key = dialog.get_api_key()
            request = SaveApiKeyRequest(
                credential_type=CredentialType.GEMINI,
                api_key=api_key
            )
            self.credential_controller.on_save_clicked(request)
            