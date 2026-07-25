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
)

_card_tab: Optional[QDockWidget] = None


def setup() -> None:
    main_window_did_init.append(_add_card_tab_action)


def _add_card_tab_action() -> None:
    action = QAction("Open AI cards tab", mw)
    action.triggered.connect(_show_card_tab)
    mw.form.menuTools.addAction(action)


def _show_card_tab() -> None:
    global _card_tab

    if _card_tab is None:
        _card_tab = _build_card_tab()
        mw.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, _card_tab)

    _card_tab.show()
    _card_tab.raise_()
    _card_tab.activateWindow()


def _build_card_tab() -> QDockWidget:
    global _word_input

    dock = QDockWidget("ankiweb_cards", mw)

    widget = QWidget()
    layout = QVBoxLayout(widget)

    layout.addWidget(QLabel("Enter word:"))

    _word_input = QLineEdit()
    _word_input.setPlaceholderText("Type something...")

    layout.addWidget(_word_input)

    dock.setWidget(widget)
    return dock