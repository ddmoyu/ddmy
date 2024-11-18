from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt, Signal
from qfluentwidgets import ImageLabel, ElevatedCardWidget, BodyLabel


class BookCard(ElevatedCardWidget):
    book_clicked = Signal(dict)

    def __init__(self, parent=None, book_data=None) -> None:
        super().__init__(parent)
        self.book_data = book_data

        print(book_data)
        self.setFixedSize(165, 243)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        image_label = ImageLabel(self)
        # image_label.setImage("")
        image_label.setFixedSize(165, 213)
        image_label.setScaledContents(True)
        main_layout.addWidget(image_label)

        title_label = BodyLabel(self)
        title_label.setText("书名")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setWordWrap(False)
        main_layout.addWidget(title_label)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.book_clicked.emit(self.book_data)
