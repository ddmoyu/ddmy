from .ui_detail import Ui_NovelDetail
from PySide6.QtWidgets import QWidget

class NovelDetail(Ui_NovelDetail, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)