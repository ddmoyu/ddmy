from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from PySide6.QtGui import QPixmap
from qfluentwidgets import (
    ImageLabel,
    CardWidget,
    CaptionLabel,
    StrongBodyLabel,
    FluentIcon,
    PushButton,
    TransparentToolButton,
)


class BookCard(CardWidget):
    book_clicked = Signal(dict)

    def __init__(self, parent=None, book_data=None) -> None:
        super().__init__(parent)
        self.book_data = book_data
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        grid_form_layout = QGridLayout(self)
        widget_body = QWidget(self)
        grid_body_layout = QGridLayout(widget_body)

        cover_label = ImageLabel(widget_body)
        pixmap = QPixmap("src/resource/images/nocover.jpg")
        scaled_pixmap = pixmap.scaled(
            QSize(90, 120),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        cover_label.setPixmap(scaled_pixmap)
        cover_label.setMaximumWidth(90)
        grid_body_layout.addWidget(cover_label, 0, 0, 1, 1)

        wgt_detail = QWidget(widget_body)
        grid_detail = QGridLayout(wgt_detail)
        grid_body_layout.addWidget(wgt_detail, 0, 1, 1, 1)

        title_label = StrongBodyLabel("title", self)
        author_label = CaptionLabel("author", self)
        intro_text = """Thorium Reader supports LCP-protected publications via an additional software component which is not available in this open-source codebase. When Thorium Reader is compiled from the open-source code without the additional production-grade library, the application can only load publications protected with the LCP "Basic Encryption Profile". For example, licenses generated by the open-source LCP server written in Go, without the patch that enables production-grade LCP Encryption Profiles.
            In order to create a production-grade LCP-compliant variant / derivation of Thorium Reader (known as a "fork"), additional confidential software components and processes must be integrated in the custom application's build / release workflow. This represents a non-trivial amount of time and effort, as well as close collaboration between the fork's development team and EDRLab's technical staff. To cover operational costs, EDRLab charges a maintenance fee. Feel free to contact EDRlab to discuss your requirements.
        """
        intro_label = QLabel(intro_text)
        intro_label.setWordWrap(True)
        grid_detail.addWidget(title_label, 0, 0, 1, 1)
        grid_detail.addWidget(author_label, 1, 0, 1, 1)
        grid_detail.addWidget(intro_label, 2, 0, 1, 1)

        grid_form_layout.addWidget(widget_body, 0, 0, 1, 1)

        read_btn = PushButton("阅读", self)
        more_btn = TransparentToolButton(FluentIcon.MORE, self)
        more_btn.setFixedSize(32, 32)
        wgt_btn = QWidget(widget_body)
        wgt_btn.setMaximumWidth(140)
        grid_btn = QGridLayout(wgt_btn)
        grid_btn.addWidget(read_btn, 0, 0, 1, 1)
        grid_btn.addWidget(more_btn, 0, 1, 1, 1)

        grid_form_layout.addWidget(wgt_btn, 0, 1, 1, 1)
        self.setFixedHeight(150)

    def on_read_triggered(self):
        print("on_read_action_triggered")

    def on_detail_triggered(self):
        print("on_detail_action_triggered")