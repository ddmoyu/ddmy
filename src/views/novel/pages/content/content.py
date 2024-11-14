from .ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget

class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)