from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QPixmap
from qfluentwidgets import (
    ImageLabel,
    ElevatedCardWidget,
    BodyLabel,
    ToolTipFilter,
    ToolTipPosition,
    RoundMenu,
    FluentIcon,
    Action,
)


class BookCard(ElevatedCardWidget):
    book_clicked = Signal(dict)

    def __init__(self, parent=None, book_data=None) -> None:
        super().__init__(parent)
        self.book_data = book_data
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 16)
        main_layout.setSpacing(10)

        image_label = ImageLabel(self)
        pixmap = QPixmap("src/resource/images/cover.jpg")
        scaled_pixmap = pixmap.scaled(
            QSize(180, 240),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        image_label.setPixmap(scaled_pixmap)

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

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent")
        if e.button() == Qt.MouseButton.LeftButton:
            self.book_clicked.emit(self.book_data)

    def contextMenuEvent(self, pos):
        menu = RoundMenu()
        read_action = Action(FluentIcon.DOCUMENT, "阅读", self)
        detail_action = Action(FluentIcon.DICTIONARY, "详情", self)
        delete_action = Action(FluentIcon.DELETE, "删除", self)
        change_action = Action(FluentIcon.GLOBE, "换源", self)
        read_action.triggered.connect(self.on_read_triggered)
        detail_action.triggered.connect(self.on_detail_triggered)
        delete_action.triggered.connect(self.on_delete_triggered)
        change_action.triggered.connect(self.on_change_triggered)
        menu.addAction(read_action)
        menu.addAction(detail_action)
        menu.addAction(delete_action)
        menu.addAction(change_action)
        menu.exec_(self.mapToGlobal(pos), ani=True)

    def on_read_triggered(self):
        print("on_read_action_triggered")

    def on_detail_triggered(self):
        print("on_detail_action_triggered")

    def on_delete_triggered(self):
        print("on_delete_action_triggered")

    def on_change_triggered(self):
        print("on_change_action_triggered")
