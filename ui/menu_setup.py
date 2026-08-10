from aqt import mw
from aqt.gui_hooks import main_window_did_init
from aqt.qt import (
    QAction,
    QDockWidget,
    Qt,
)

from ..app_factory import build_card_tab

# Global variable to hold the reference to the card tab. This is used to ensure that only one instance of the card tab exists at any given time.
_card_tab: QDockWidget | None = None
            
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

# This function builds the AI cards tab and returns it as a QDockWidget.
# The layers of the tab are built and wired together using the build_card_tab function from the app_factory module.
def _build_card_tab() -> QDockWidget:
    dock = QDockWidget("ankiweb_cards", mw)
    dock.setObjectName("ankiweb_cardsDock")

    dock.setAllowedAreas(
        Qt.DockWidgetArea.LeftDockWidgetArea
        | Qt.DockWidgetArea.RightDockWidgetArea
    )
    
    card_tab = build_card_tab()
    
    dock.setWidget(card_tab)

    return dock