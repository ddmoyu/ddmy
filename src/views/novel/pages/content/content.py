from qfluentwidgets import FluentIcon
from src.views.novel.pages.content.ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from src.views.novel.utils.utils import parse_content
from src.common.signal_bus import signalBus


class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.initUI()
        self.initSignal()

    def initUI(self):
        self.wgt_style.hide()
        self.btn_view.setIcon(FluentIcon.VIEW)
        self.btn_style.setIcon(FluentIcon.SETTING)
        self.btn_next_chapter.setIcon(FluentIcon.PAGE_RIGHT)
        self.btn_prev_chapter.setIcon(FluentIcon.PAGE_LEFT)

    def initSignal(self):
        self.btn_view.clicked.connect(self.on_btn_view_handler)
        self.btn_style.clicked.connect(self.on_btn_style_handler)
        self.pushButton_3.clicked.connect(
            lambda: signalBus.wv_navigate.emit(
                "https://www.zhongyi6.com/chapter/read/1734/36970"
            )
        )
        signalBus.wv_get_html.connect(self.render_content)

    def on_btn_view_handler(self):
        self.frame_top.hide()
        self.frame_footer.hide()
        self.wgt_style.hide()

    def on_btn_style_handler(self):
        if self.wgt_style.isHidden():
            self.wgt_style.show()
        else:
            self.wgt_style.hide()

    def render_content(self, html):
        text = parse_content(html, "#body@html")
        # text = parse_content(html, 'p:nth-of-type(n+2)@text')
        # text = parse_content(html, '.rxx-badge@text')
        self.textBrowser.setMarkdown(text)
        font = QFont("霞鹜文楷", 16)
        self.textBrowser.setFont(font)

        # self.textBrowser.setStyleSheet("#textBrowser{}")
