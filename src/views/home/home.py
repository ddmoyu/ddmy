# coding:utf-8
from qfluentwidgets import ScrollArea
from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from src.layout.card import CardView

class HomeInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        self.init_widget()
        self.load_views()

    def init_widget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def load_views(self):
        novel = CardView("Novel", self.view)
        novel.addCard(
            "",
            "Novel",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'NovelInterface'
        )
        self.vBoxLayout.addWidget(novel)

        photo = CardView("Photo", self.view)
        photo.addCard(
            "",
            "Photo",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'PhotoInterface'
        )
        self.vBoxLayout.addWidget(photo)