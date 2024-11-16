from .ui_list import Ui_NovelList
from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtCore import Qt
from .tools import (fetch_json_async, parser_exploreUrl)
from qasync import asyncSlot

class NovelList(Ui_NovelList, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)
        self.json_data = []

        self.init_ui()
        self.init_signal()
        self.init_list()

    def init_ui(self) -> None:
        self.book_footer.hide()

    def init_signal(self) -> None:
        self.list.itemClicked.connect(self.on_list_item_clicked)
        self.category.itemClicked.connect(self.on_category_item_clicked)

    @asyncSlot()
    async def init_list(self) -> None:
        content = await fetch_json_async("https://www.yckceo.com/yuedu/shuyuans/json/id/663.json")
        if content is None:
            return
        self.json_data = []
        for item in content:
            book_name = item["bookSourceName"]
            book_type = item["bookSourceType"]
            if book_type == 0:
                self.list.addItem(book_name)
                self.json_data.append(item)

    def on_list_item_clicked(self, item) -> None:
        self.category.clear()
        explore_url = None
        bookSourceUrl = None
        for i in range(len(self.json_data)):
            if self.json_data[i]["bookSourceName"] == item.text():
                source = self.json_data[i]
                bookSourceUrl = source["bookSourceUrl"]
                if 'exploreUrl' in source:
                    explore_url = self.json_data[i]["exploreUrl"]
                if explore_url is None:
                    return
                break

        category_list = parser_exploreUrl(explore_url)
        if not category_list:
            return

        for category in category_list:
            name = category["name"]
            category_item = QListWidgetItem(name)
            category_item.setData(Qt.UserRole, category["url"])
            category_item.setData(Qt.UserRole + 1, bookSourceUrl)
            self.category.addItem(category_item)
        self.category.scrollToTop()

    def on_category_item_clicked(self, item) -> None:
        print(item.text())
        url = item.data(Qt.UserRole)
        bookSourceUrl = item.data(Qt.UserRole + 1)
        print(url)
        print(bookSourceUrl)