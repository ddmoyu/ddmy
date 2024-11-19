from qfluentwidgets import FluentIcon

from src.common.tools import load_json
from .ui_explore import Ui_NovelExplore
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLayout
from PySide6.QtCore import Qt
from .tools import parser_exploreUrl
from .components.book_card import BookCard


class NovelList(Ui_NovelExplore, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.json_data = []

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

    def init_list(self) -> None:
        sources = load_json("novel_sources.json")
        if not sources:
            return
        self.list.clear()
        self.json_data = sources
        for source in sources:
            self.list.addItem(source.get("bookSourceName"))

    def on_list_item_clicked(self, item) -> None:
        self.category.clear()
        explore_url = None
        book_source_url = None
        for i in range(len(self.json_data)):
            if self.json_data[i]["bookSourceName"] == item.text():
                source = self.json_data[i]
                book_source_url = source["bookSourceUrl"]
                if "exploreUrl" in source:
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
            category_item.setData(Qt.ItemDataRole.UserRole, category["url"])
            category_item.setData(Qt.ItemDataRole.UserRole + 1, book_source_url)
            self.category.addItem(category_item)
        self.category.scrollToTop()

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
