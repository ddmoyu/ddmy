from .ui_bookshelf import Ui_NovelBookshelf
from PySide6.QtWidgets import QWidget

class NovelBookshelf(Ui_NovelBookshelf, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)
