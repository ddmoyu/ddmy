from .ui_search import Ui_NovelSearch
from PySide6.QtWidgets import QWidget, QSizePolicy

class NovelSearch(Ui_NovelSearch, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)
        self.container.hide()
        self.le_search.returnPressed.connect(self.searchEventHandler)
        self.le_search.textChanged.connect(self.searchChangedHandler)

        print(self.parent.size())
        self.resize(self.parent.size())
        print(self.size())

    def searchEventHandler(self):
        self.container.show()

    def searchChangedHandler(self):
        if len(self.le_search.text()) == 0:
            self.container.hide()
