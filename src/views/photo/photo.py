from .ui_photo import Ui_Form
from src.layout.layout import LayoutInterface

class PhotoInterface(LayoutInterface):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setObjectName("PhotoInterface")