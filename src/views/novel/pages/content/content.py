from typing import Optional
from qfluentwidgets import FluentIcon
from src.views.novel.pages.content.ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from src.views.novel.utils.u_content import parse_content
from src.common.signal_bus import signalBus, WebviewType
from src.views.novel.utils.u_content import get_toc_list
from src.views.novel.data_class.source import RuleSource


class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.init_ui()
        self.init_signal()

        self.current_rule_source = Optional[RuleSource]

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
        signalBus.wv_html.connect(self.get_wv_html)
        signalBus.novel_rule_source.connect(self.get_novel_rule_source)

    def get_novel_rule_source(self, rule_source):
        print("rule_source", rule_source)
        self.current_rule_source = rule_source

    def get_wv_html(self, wv_type: WebviewType, html):
        # print("content", html)
        if wv_type == WebviewType.TOC:
            rule_toc = self.current_rule_source.rule_toc
            print("rule_toc", rule_toc)
            toc_list = get_toc_list(html, rule_toc)
            if not toc_list:
                return
            print("toc_list", toc_list)
            for toc in toc_list:
                name = toc.chapter_name
                print(name)
            #     category_item = QListWidgetItem(name)
            #     category_item.setData(Qt.ItemDataRole.UserRole, category)
            #     self.category.addItem(category_item)
            # self.category.scrollToTop()
            # self.category_loading.hide_loading()

    def get_book_info(self, book_url: str):
        print("book_url", book_url)
        url = "https://www.66story.com" + book_url
        signalBus.wv_url.emit(WebviewType.TOC, url)
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
