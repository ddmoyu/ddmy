from .ui_live import Ui_Form
from src.layout.layout import LayoutInterface

class LiveInterface(LayoutInterface):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName("LiveInterface")