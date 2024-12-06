from typing import Optional
from qfluentwidgets import FluentIcon
from urllib.parse import urljoin

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QListWidgetItem

from src.views.novel.data_class.explore import DataExplore
from src.views.novel.pages.content.ui_content import Ui_NovelContent
from src.views.novel.utils.u_content import get_toc_list, get_content
from src.views.novel.data_class.source import RuleSource
from src.views.novel.data_class.toc import DataToc
from src.common.signal_bus import signalBus, WebviewType
from src.components.loading import LoadingOverlay


class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.toc_loading = LoadingOverlay(self.wgt_toc)

        self.current_rule_source = Optional[RuleSource]

        self.init_ui()
        self.init_signal()

    def init_ui(self):
        self.wgt_style.hide()
        self.wgt_toc.hide()
        self.toc_loading.hide_loading()
        self.btn_chapter.setIcon(FluentIcon.MENU)
        self.btn_view.setIcon(FluentIcon.VIEW)
        self.btn_style.setIcon(FluentIcon.SETTING)
        self.btn_next_chapter.setIcon(FluentIcon.PAGE_RIGHT)
        self.btn_prev_chapter.setIcon(FluentIcon.PAGE_LEFT)

    def init_signal(self):
        self.btn_view.clicked.connect(self.on_btn_view_handler)
        self.btn_style.clicked.connect(self.on_btn_style_handler)
        self.btn_chapter.clicked.connect(self.on_btn_chapter_handler)
        self.lw_toc.itemClicked.connect(self.on_toc_item_clicked)
        signalBus.novel_bool_url.connect(self.get_book_toc)
        signalBus.wv_html.connect(self.get_wv_html)
        signalBus.novel_rule_source.connect(self.get_novel_rule_source)

    def get_novel_rule_source(self, rule_source):
        self.current_rule_source = rule_source

    def get_wv_html(self, wv_type: WebviewType, html):
        if wv_type == WebviewType.TOC:
            rule_toc = self.current_rule_source.rule_toc
            self.lw_toc.clear()
            toc_list = get_toc_list(html, rule_toc)
            if not toc_list:
                return
            toc_list.reverse()
            for toc in toc_list:
                name = toc.chapter_name
                toc_item = QListWidgetItem(name)
                toc_item.setData(Qt.ItemDataRole.UserRole, toc)
                self.lw_toc.addItem(toc_item)

            self.lw_toc.scrollToTop()
            self.toc_loading.hide_loading()
        if wv_type == WebviewType.CONTENT:
            rule_content = self.current_rule_source.rule_content
            data = get_content(html, rule_content)
            self.render_content(data.content)

    def get_book_toc(self, data: DataExplore):
        url = data.toc_url
        origin = self.current_rule_source.book_source_url
        if not url.startswith("http"):
            url = urljoin(origin, url)
        self.lw_toc.clear()
        self.toc_loading.show_loading()
        signalBus.wv_url.emit(WebviewType.TOC, url)

    def on_btn_view_handler(self):
        # self.frame_top.hide()
        # self.frame_footer.hide()
        self.wgt_style.show()
        self.wgt_toc.show()
        pass

    def on_btn_chapter_handler(self):
        if self.wgt_toc.isVisible():
            self.wgt_toc.hide()
        else:
            self.wgt_toc.show()

    def on_btn_style_handler(self):
        if self.wgt_style.isVisible():
            self.wgt_style.hide()
        else:
            self.wgt_style.show()

    def on_toc_item_clicked(self, item: QListWidgetItem):
        toc: DataToc = item.data(Qt.ItemDataRole.UserRole)
        name = toc.chapter_name
        self.lb_chapter.setText(name)
        url = toc.chapter_url
        if url.startswith("http"):
            final_url = url
        else:
            final_url = urljoin(self.current_rule_source.book_source_url, url)
        signalBus.wv_url.emit(WebviewType.CONTENT, final_url)

    def render_content(self, html):
        font = QFont("霞鹜文楷", 16)
        self.textBrowser.setFont(font)
        self.textBrowser.setMarkdown(html)

        # self.textBrowser.setStyleSheet("#textBrowser{}")
