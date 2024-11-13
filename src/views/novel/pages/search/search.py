from .ui_search import Ui_NovelSearch
from PySide6.QtWidgets import QWidget, QSizePolicy

class NovelSearch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.ui = Ui_NovelSearch()
        self.ui.setupUi(self)

    def showEvent(self, event):
        self.resize(self.parent.size())
