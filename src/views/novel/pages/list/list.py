from .ui_list import Ui_NovelList
from PySide6.QtWidgets import QWidget

class NovelList(Ui_NovelList, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)