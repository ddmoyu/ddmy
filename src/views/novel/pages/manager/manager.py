from .ui_manager import Ui_NovelManager
from PySide6.QtWidgets import QWidget

class NovelManager(Ui_NovelManager, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)