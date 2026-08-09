from typing import Optional

from aqt import mw
from aqt.gui_hooks import main_window_did_init
from aqt.qt import (
    QAction,
    QDialog,
    QDialogButtonBox,
    QDockWidget,
    Qt,
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

from ..app_factory import build_card_controller_if_configured, build_credential_controller

# Global variable to hold the reference to the card tab. This is used to ensure that only one instance of the card tab exists at any given time.
_card_tab: Optional[QDockWidget] = None

# This class represents a dialog window that prompts the user to enter their API key. It contains a text input for the API key and buttons to save or cancel the action.
class ApiKeyDialog(QDialog):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        
        self.setWindowTitle("API Keys")
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        # Label
        layout.addWidget(QLabel("Enter your Google Gemini API key:"))

        # API key input
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter Google Gemini API key...")
        
        # Hide the API key characters
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.api_key_input)

        # Save / Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def get_api_key(self) -> str:
        return self.api_key_input.text().strip()

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
        
        if not self.card_controller:
            self.error_label.setText("AI API key is not configured. Please set it up first.")
            self.error_label.setVisible(True)
            return
        
        selected_deck = self.deck_dropdown.currentText()
        request = CreateCardRequest(
            deck_name=selected_deck,
            word=self.word_input.text()
        )
        
        result = self.card_controller.on_generate_clicked(request)
        
        if not result or not result.success:
            self.error_label.setText(result.error if result else "Failed to generate card.")
            self.error_label.setVisible(True)
        else:
            self.result_label.setText(f"A card generated successfully for the word '{result.card.word_trans}'!")
            self.result_label.setVisible(True)
    
    def _handle_api_clicked(self) -> None:
        dialog = ApiKeyDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            api_key = dialog.get_api_key()
            request = SaveApiKeyRequest(
                key_name="GEMINI_API_KEY",
                api_key=api_key
            )
            self.credential_controller.on_save_clicked(request)
            
# This function is called when the add-on is loaded. 
# It sets up the necessary hooks and actions for the add-on.
def setup() -> None:
    main_window_did_init.append(_add_card_tab_action)

# This function adds an action to the Anki Tools menu that allows users to open the AI cards tab.
def _add_card_tab_action() -> None:
    action = QAction("Create AI cards", mw)
    action.triggered.connect(_show_card_tab)
    mw.form.menuTools.addAction(action)

# This function shows the AI cards tab. If the tab doesn't exist yet, it creates it first.
def _show_card_tab() -> None:
    global _card_tab

    if _card_tab is None:
        _card_tab = _build_card_tab()
        mw.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea,
            _card_tab,
        )

    _card_tab.show()
    _card_tab.raise_()
    _card_tab.activateWindow()

# This function builds the AI cards tab, which is a dockable widget in the Anki interface.
def _build_card_tab() -> QDockWidget:
    dock = QDockWidget("ankiweb_cards", mw)
    dock.setObjectName("ankiweb_cardsDock")

    dock.setAllowedAreas(
        Qt.DockWidgetArea.LeftDockWidgetArea
        | Qt.DockWidgetArea.RightDockWidgetArea
    )

    credential_controller = build_credential_controller()
    card_controller = build_card_controller_if_configured(credential_controller)
    
    card_tab = CardTab(card_controller=card_controller,
                       credential_controller=credential_controller)
    
    dock.setWidget(card_tab)

    return dock