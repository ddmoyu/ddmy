from qfluentwidgets import (ScrollArea)
from .ui_settings import Ui_Form

class SettingsInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
