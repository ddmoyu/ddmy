from typing import Optional

from qfluentwidgets import FluentIcon

from src.common.tools import load_json
from .ui_explore import Ui_NovelExplore
from PySide6.QtWidgets import QWidget, QLayout, QListWidgetItem
from PySide6.QtCore import Qt
from src.components.book_card import BookCard
from src.views.novel.data.entities.source_entity import SourceEntity
from src.common.signal_bus import signalBus, WebviewType
from src.views.novel.utils.u_explore import get_category_list


class NovelList(Ui_NovelExplore, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.source_list = []
        self.source_list_dict = {}
        self.current_source = Optional[SourceEntity]
        self.current_category = None
        self.current_explore = None

        self.init_ui()
        self.init_signal()
        self.init_list()

    def init_ui(self) -> None:
        self.book_footer.hide()
        self.btn_prev.setIcon(FluentIcon.LEFT_ARROW)
        self.btn_next.setIcon(FluentIcon.RIGHT_ARROW)

    def init_signal(self) -> None:
        self.list.itemClicked.connect(self.on_list_item_clicked)
        self.category.itemClicked.connect(self.on_category_item_clicked)
        signalBus.wv_html.connect(self.get_wv_html)

    def init_list(self) -> None:
        sources = load_json("novel_sources.json")
        if not sources:
            return
        self.source_list = sources
        self.source_list_dict = {
            source.get("bookSourceName"): source for source in sources
        }
        self.list.clear()
        for source in sources:
            self.list.addItem(source.get("bookSourceName"))

    def on_list_item_clicked(self, item) -> None:
        self.category.clear()
        source = self.source_list_dict.get(item.text())
        if source is None:
            return
        print(source)
        self.current_source = SourceEntity.from_json(source)
        self.current_category = self.current_source.rule_category
        self.current_explore = self.current_source.rule_explore

        print(self.current_category.url)

        signalBus.wv_url.emit(WebviewType.CATEGORY, self.current_category.url)
        # signalBus.wv_navigate.emit(self.current_category.url)

        pass
        # explore_url = None
        # for i in range(len(self.json_data)):
        #     if self.json_data[i]["bookSourceName"] == item.text():
        #         source = self.json_data[i]
        #         book_source_url = source["bookSourceUrl"]
        #         if "exploreUrl" in source:
        #             explore_url = self.json_data[i]["exploreUrl"]
        #         if explore_url is None:
        #             return
        #         break
        #
        # category_list = parser_exploreUrl(explore_url)
        # if not category_list:
        #     return
        #
        # for category in category_list:
        #     name = category["name"]
        #     category_item = QListWidgetItem(name)
        #     category_item.setData(Qt.ItemDataRole.UserRole, category["url"])
        #     category_item.setData(Qt.ItemDataRole.UserRole + 1, book_source_url)
        #     self.category.addItem(category_item)
        # self.category.scrollToTop()

    def get_wv_html(self, wv_type: WebviewType, html):
        if wv_type == WebviewType.CATEGORY:
            # print("category", html)
            category_list = get_category_list(html, self.current_category)
            print("category_list: ", category_list)
            if not category_list:
                return
            for category in category_list:
                name = category["name"]
                category_item = QListWidgetItem(name)
                category_item.setData(Qt.ItemDataRole.UserRole, category["url"])
                category_item.setData(
                    Qt.ItemDataRole.UserRole + 1, self.current_source.book_source_url
                )
                self.category.addItem(category_item)
            self.category.scrollToTop()
        elif wv_type == WebviewType.EXPLORE:
            print("explore", html)

    def on_category_item_clicked(self, item) -> None:
        print(item.text())
        url = item.data(Qt.ItemDataRole.UserRole)
        book_source_url = item.data(Qt.ItemDataRole.UserRole + 1)
        print(url)
        print(book_source_url)
        self.render_book_list(url)

    def clear_layout(self, layout: QLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()  # 异步删除小部件
                else:
                    layout.removeItem(item)
                    if item.layout():
                        self.clear_layout(item.layout())

    def render_book_list(self, data) -> None:
        self.clear_layout(self.qvl_list)
        self.qvl_list.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.qvl_list.setSpacing(8)
        self.book_footer.show()
        for item in range(21):
            book = BookCard()
            self.qvl_list.addWidget(book)
