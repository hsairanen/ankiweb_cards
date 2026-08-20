from aqt.qt import (
    QDialog,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
)

# This class represents a dialog window that prompts the user to enter API keys.
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
        #self.api_key_input.setPlaceholderText("Enter Google Gemini API key...")
        
        # Hide the API key characters
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.api_key_input)

        layout.addWidget(QLabel("Enter your image bank Pexels API key:"))

        self.image_bank_api_key_input = QLineEdit()
        #self.image_bank_api_key_input.setPlaceholderText("Enter image bank API key...")
        self.image_bank_api_key_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.image_bank_api_key_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def get_api_key(self) -> str:
        return self.api_key_input.text().strip()

    def get_image_bank_api_key(self) -> str:
        return self.image_bank_api_key_input.text().strip()
