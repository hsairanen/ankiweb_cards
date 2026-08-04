from typing import Optional

from aqt import mw
from aqt.gui_hooks import main_window_did_init
from aqt.qt import (
    QAction,
    QDockWidget,
    Qt,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QLabel,
    QPushButton,
)

from ..app_factory import build_card_controller
from ..controller.CardController import CardController

# Global variable to hold the reference to the card tab. This is used to ensure that only one instance of the card tab exists at any given time.
_card_tab: Optional[QDockWidget] = None

# This class represents the card tab in the Anki interface. It contains a text input for the user to enter a word and a button to generate cards based on that word.
class CardTab(QWidget):
    def __init__(self, controller: CardController):
        super().__init__()

        self.controller = controller

        # Creates a vertical layout - places components on top of each other
        layout = QVBoxLayout(self)

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
        result = self.controller.on_generate_clicked(self.word_input.text())
        if not result.success:
            self.error_label.setText(result.error)
            self.error_label.setVisible(True)
        else:
            self.result_label.setText(f"A card generated successfully for the word '{result.card.word_trans}'!")
            self.result_label.setVisible(True)

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

    controller = build_card_controller()

    dock.setWidget(CardTab(controller))

    return dock