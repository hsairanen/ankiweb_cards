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

from ..controller.cardController import cardController


_card_tab: Optional[QDockWidget] = None


class cardTab(QWidget):
    def __init__(self, controller: cardController):
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

        # Create generate button, connect the button click and add the button to the layout
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.on_generate_clicked)
        layout.addWidget(self.generate_button)

    def on_generate_clicked(self) -> None:
        # Get the word from the input field and strip any leading/trailing whitespace
        word = self.word_input.text().strip()

        if word:
            self.controller.create_cards(word)

# This function is called when the add-on is loaded. 
# It sets up the necessary hooks and actions for the add-on.
def setup() -> None:
    main_window_did_init.append(_add_card_tab_action)

# This function adds an action to the Anki Tools menu that allows users to open the AI cards tab.
def _add_card_tab_action() -> None:
    action = QAction("Open AI cards tab", mw)
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

    controller = cardController()

    dock.setWidget(cardTab(controller))

    return dock