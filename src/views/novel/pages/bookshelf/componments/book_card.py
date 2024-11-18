from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt, Signal, QSize


from qfluentwidgets import (
    ImageLabel,
    ElevatedCardWidget,
    BodyLabel,
    ToolTipFilter,
    ToolTipPosition,
)


class BookCard(ElevatedCardWidget):
    book_clicked = Signal(dict)

    def __init__(self, parent=None, book_data=None) -> None:
        super().__init__(parent)
        self.book_data = book_data

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 16)
        main_layout.setSpacing(10)

        image_label = ImageLabel(self)
        image_label.setImage("src/resource/images/cover.jpg")
        image_label.setScaledSize(QSize(180, 240))
        image_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        image_label.setBorderRadius(10, 10, 0, 0)
        main_layout.addWidget(image_label)

        title_label = BodyLabel(self)
        font_metrics = title_label.fontMetrics()
        elided_text = font_metrics.elidedText(
            "很长很长很长很长很长很长的名字", Qt.TextElideMode.ElideRight, 160
        )
        title_label.setToolTip("很长很长很长很长很长很长的名字")
        title_label.setToolTipDuration(1000)
        title_label.installEventFilter(
            ToolTipFilter(title_label, showDelay=300, position=ToolTipPosition.BOTTOM)
        )
        title_label.setText(elided_text)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(False)
        main_layout.addWidget(title_label)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.book_clicked.emit(self.book_data)
