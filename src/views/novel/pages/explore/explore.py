from typing import Optional, List
from urllib.parse import urljoin

from qfluentwidgets import FluentIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLayout, QListWidgetItem

from src.common.tools import load_json
from src.components.book_card import BookCard
from src.components.loading import LoadingOverlay
from src.common.signal_bus import signalBus, WebviewType

from src.views.novel.pages.explore.ui_explore import Ui_NovelExplore
from src.views.novel.utils.u_explore import get_category_list, get_explore_list 
from src.views.novel.data_class.category import RuleCategory, DataCategory
from src.views.novel.data_class.explore import RuleExplore, DataExplore
from src.views.novel.data_class.source import RuleSource, DataSource


class NovelList(Ui_NovelExplore, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)

        self.source_list = Optional[List[RuleSource]]
        self.current_rule_source = Optional[RuleSource]
        self.current_rule_category = Optional[RuleCategory]
        self.current_rule_explore = Optional[RuleExplore]

        self.book_page_number = 1
        self.prev_url = ""
        self.next_url = ""
        self.category_loading = LoadingOverlay(self.category)
        self.explore_loading = LoadingOverlay(self.book_list)

        self.init_ui()
        self.init_signal()
        self.init_sources_list()

    def init_ui(self) -> None:
        self.book_footer.hide()
        self.btn_prev.setIcon(FluentIcon.LEFT_ARROW)
        self.btn_next.setIcon(FluentIcon.RIGHT_ARROW)

    def init_signal(self) -> None:
        self.list.itemClicked.connect(self.on_sources_list_item_clicked)
        self.category.itemClicked.connect(self.on_category_item_clicked)
        self.btn_prev.clicked.connect(self.on_prev_clicked)
        self.btn_next.clicked.connect(self.on_next_clicked)
        signalBus.wv_html.connect(self.get_wv_html)

    def get_wv_html(self, wv_type: WebviewType, html):
        if wv_type == WebviewType.CATEGORY:
            category_list = get_category_list(html, self.current_rule_category)
            if not category_list:
                return
            for category in category_list:
                name = category.category_name
                category_item = QListWidgetItem(name)
                category_item.setData(Qt.ItemDataRole.UserRole, category)
                self.category.addItem(category_item)
            self.category.scrollToTop()
            self.category_loading.hide_loading()
        elif wv_type == WebviewType.EXPLORE:
            explore_list = get_explore_list(html, self.current_rule_explore)
            if not explore_list:
                return
            self.prev_url = explore_list[0].prev_url
            self.next_url = explore_list[0].next_url
            self.render_book_list(explore_list)
            self.explore_loading.hide_loading()

    def init_sources_list(self) -> None:
        json_source_lists = load_json("novel_sources.json")
        if not json_source_lists:
            return
        self.source_list = json_source_lists
        self.list.clear()
        for json_source in json_source_lists:
            source = RuleSource.from_json(json_source)
            if not source.enabled:
                continue
            source_item = QListWidgetItem(source.book_source_name)
            source_item.setData(Qt.ItemDataRole.UserRole, source)
            self.list.addItem(source_item)

    def on_sources_list_item_clicked(self, item) -> None:
        self.category_loading.show_loading()
        self.category.clear()
        source: DataSource = item.data(Qt.ItemDataRole.UserRole)
        if source is None:
            return
        self.current_rule_source = source
        self.current_rule_category = self.current_rule_source.rule_category
        self.current_rule_explore = self.current_rule_source.rule_explore
        signalBus.wv_url.emit(WebviewType.CATEGORY, self.current_rule_category.url)

    def on_category_item_clicked(self, item) -> None:
        self.explore_loading.show_loading()
        category: DataCategory = item.data(Qt.ItemDataRole.UserRole)
        url = category.category_url
        book_source_url = self.current_rule_source.book_source_url
        if url.startswith("http"):
            final_url = url
        else:
            final_url = urljoin(book_source_url, url)
        signalBus.wv_url.emit(WebviewType.EXPLORE, final_url)
        self.book_page_number = 1

    def clear_layout(self, layout: QLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    layout.removeItem(item)
                    if item.layout():
                        self.clear_layout(item.layout())

    def render_book_list(self, data_list: List[DataExplore]):
        self.clear_layout(self.qvl_list)
        self.qvl_list.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.qvl_list.setSpacing(8)
        self.book_footer.show()
        self.lb_page.setText(f'第 {self.book_page_number} 页')
        for book in data_list:
            book = BookCard(parent=self, book_data=book, source=self.current_rule_source)
            self.qvl_list.addWidget(book)
        self.book_list.verticalScrollBar().setValue(0)

    def on_prev_clicked(self):
        if self.book_page_number == 1:
            return
        self.book_page_number -= 1
        self.lb_page.setText(f'第 {self.book_page_number} 页')
        if self.prev_url.startswith("http"):
            final_url = self.prev_url
        else:
            book_source_url = self.current_rule_source.book_source_url
            final_url = urljoin(book_source_url, self.prev_url)
        self.explore_loading.show_loading()
        signalBus.wv_url.emit(WebviewType.EXPLORE, final_url)

    def on_next_clicked(self):
        self.book_page_number += 1
        self.lb_page.setText(f'第 {self.book_page_number} 页')
        if self.next_url.startswith("http"):
            final_url = self.next_url
        else:
            book_source_url = self.current_rule_source.book_source_url
            final_url = urljoin(book_source_url, self.next_url)
        self.explore_loading.show_loading()
        signalBus.wv_url.emit(WebviewType.EXPLORE, final_url)
