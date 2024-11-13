from .ui_novel import Ui_Novel
from src.layout.layout import LayoutInterface
from .pages.search.search import NovelSearch
from enum import Enum

class NovelPage(Enum):
    LIST = 0
    MANAGER = 1
    SEARCH = 2
    DETAIL = 3
    BOOKSHELF = 4
    BOOKMARK = 5
    CONTENT = 6

class NovelInterface(LayoutInterface):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.ui = Ui_Novel()
        self.ui.setupUi(self)
        self.setObjectName("NovelInterface")

        self.search = NovelSearch(self.ui.stack)

        self.ui.stack.setCurrentWidget(self.search)
        self.ui.stack.setCurrentIndex(NovelPage.SEARCH.value)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        current_wgt = self.ui.stack.currentWidget()
        if current_wgt.objectName() == 'search':
            self.search.resize(self.ui.stack.size())