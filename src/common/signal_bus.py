# coding: utf-8
from PySide6.QtCore import QObject, Signal
from enum import Enum
from src.views.novel.data_class.source import RuleSource


class WebviewType(Enum):
    URL = "default"
    CATEGORY = "category"
    EXPLORE = "explore"
    TOC = "toc"


class SignalBus(QObject):
    """Signal bus"""

    switchToSampleCard = Signal(str)
    micaEnableChanged = Signal(bool)

    # webview signal
    wv_load_finished = Signal(bool)
    wv_url = Signal(WebviewType, str)
    wv_html = Signal(WebviewType, str)

    # novel signal
    novel_change_page = Signal(str)
    novel_bool_url = Signal(str)
    novel_rule_source = Signal(RuleSource)


signalBus = SignalBus()
