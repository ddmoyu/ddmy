# coding: utf-8
from PySide6.QtCore import QObject, Signal


class SignalBus(QObject):
    """Signal bus"""

    switchToSampleCard = Signal(str)
    micaEnableChanged = Signal(bool)

    # webview signal
    wv_load_finished = Signal(bool)
    wv_navigate = Signal(str)
    wv_get_html = Signal(str)


signalBus = SignalBus()
