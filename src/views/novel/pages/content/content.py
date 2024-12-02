from qfluentwidgets import FluentIcon
from src.views.novel.pages.content.ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from src.views.novel.utils.u_content import parse_content
from src.common.signal_bus import signalBus


class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_ui()
        self.init_signal()

    def init_ui(self):
        self.wgt_style.hide()
        self.wgt_toc.hide()
        self.btn_chapter.setIcon(FluentIcon.MENU)
        self.btn_view.setIcon(FluentIcon.VIEW)
        self.btn_style.setIcon(FluentIcon.SETTING)
        self.btn_next_chapter.setIcon(FluentIcon.PAGE_RIGHT)
        self.btn_prev_chapter.setIcon(FluentIcon.PAGE_LEFT)

    def init_signal(self):
        self.btn_view.clicked.connect(self.on_btn_view_handler)
        self.btn_style.clicked.connect(self.on_btn_style_handler)
        # self.pushButton_3.clicked.connect(
        #     lambda: signalBus.wv_navigate.emit(
        #         "https://www.zhongyi6.com/chapter/read/1734/36970"
        #     )
        # )
        # signalBus.wv_get_html.connect(self.render_content)
        signalBus.novel_bool_url.connect(self.get_book_info)

    def get_book_info(self, book_url: str):
        print('book_url', book_url)
        pass

    def on_btn_view_handler(self):
        # self.frame_top.hide()
        # self.frame_footer.hide()
        self.wgt_style.show()
        self.wgt_toc.show()
        pass

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
