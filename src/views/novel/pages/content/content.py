from src.views.novel.pages.content.ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from src.views.novel.utils.utils import parse_content
from src.common.signal_bus import signalBus


class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.pushButton_3.clicked.connect(
            lambda: signalBus.wv_navigate.emit(
                "https://www.zhongyi6.com/chapter/read/1734/36970"
            )
        )
        signalBus.wv_get_html.connect(self.render_content)

    def render_content(self, html):
        text = parse_content(html, "#body@html")
        # text = parse_content(html, 'p:nth-of-type(n+2)@text')
        # text = parse_content(html, '.rxx-badge@text')
        self.textBrowser.setMarkdown(text)
        font = QFont("霞鹜文楷", 16)
        self.textBrowser.setFont(font)

        # self.textBrowser.setStyleSheet("#textBrowser{}")
