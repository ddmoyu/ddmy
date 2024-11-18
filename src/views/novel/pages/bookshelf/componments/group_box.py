from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import SubtitleLabel, FlowLayout
from .book_card import BookCard


class GroupBox(QWidget):
    def __init__(self, parent=None, group_data=None) -> None:
        super().__init__(parent)

        main_layout = QVBoxLayout(self)
        group_label = SubtitleLabel("默认")
        group_label.setAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        main_layout.addWidget(group_label)

        books = QWidget()
        book_layout = FlowLayout(books, True)
        book_layout.setContentsMargins(0, 0, 0, 0)
        book_layout.setVerticalSpacing(20)
        book_layout.setHorizontalSpacing(20)
        for i in range(30):
            # book_data = {"name": "书籍名称", "cover": "https://picsum.photos/480"}
            book = BookCard()
            book_layout.addWidget(book)

        main_layout.addWidget(books)
        main_layout.setContentsMargins(0, 0, 0, 30)
        main_layout.setSpacing(20)
