from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPixmap, QFontMetrics, QTextOption
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

        cover_label = ImageLabel()
        title_label = StrongBodyLabel("title", self)
        author_label = CaptionLabel("author", self)
        intro_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius nonummy ac, nonummy ut, tortor. Pellentesque ornare sem lacus, ut luctus elit fermentum non, dignissim."

        # self.intro_label = QTextEdit()
        # self.intro_label.setReadOnly(True)
        # self.intro_label.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        # self.intro_label.setWordWrapMode(
        #     QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere
        # )

        # self.intro_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.intro_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.intro_label.setText(intro_text)
        # self.intro_label = BodyLabel()
        # self.intro_label.setWordWrap(True)
        # self.intro_label.setText(intro_text)
        # self.intro_label.setTextInteractionFlags(
        #     Qt.TextInteractionFlag.NoTextInteraction
        # )
        # self.set_intro_text(intro_text)

        read_btn = PushButton("阅读", self)
        more_btn = TransparentToolButton(FluentIcon.MORE, self)

        h_box_layout = QHBoxLayout(self)
        v_box_layout = QVBoxLayout()

        self.setFixedHeight(144)

        pixmap = QPixmap("src/resource/images/nocover.jpg")
        scaled_pixmap = pixmap.scaled(
            QSize(90, 120),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        cover_label.setPixmap(scaled_pixmap)

        h_box_layout.setContentsMargins(16, 12, 10, 12)
        h_box_layout.setSpacing(15)
        h_box_layout.addWidget(cover_label)

        v_box_layout.setContentsMargins(0, 0, 0, 0)
        v_box_layout.setSpacing(6)
        v_box_layout.addWidget(title_label)
        v_box_layout.addWidget(author_label)
        v_box_layout.addWidget(self.intro_label)
        v_box_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        h_box_layout.addLayout(v_box_layout)

        # h_box_layout.addStretch(1)
        h_box_layout.addWidget(read_btn, 0, Qt.AlignRight)
        h_box_layout.addWidget(more_btn, 0, Qt.AlignRight)

        more_btn.setFixedSize(32, 32)

    def set_intro_text(self, text):
        font = self.intro_label.font()
        metrics = QFontMetrics(font)
        # 计算每行文本的高度
        line_height = metrics.height()
        # 计算3行文本的高度
        max_height = line_height * 3

        # 计算在3行内能显示的最大字符数
        available_width = self.intro_label.width()
        max_chars_per_line = metrics.horizontalAdvance(
            "W" * (available_width // metrics.horizontalAdvance("W"))
        )
        max_chars = max_chars_per_line * 3

        # 截断文本
        if metrics.boundingRect(text).height() > max_height:
            elided_text = metrics.elidedText(
                text, Qt.TextElideMode.ElideRight, max_chars
            )
            self.intro_label.setText(elided_text)
        else:
            self.intro_label.setText(text)

    def on_read_triggered(self):
        print("on_read_action_triggered")

    def on_detail_triggered(self):
        print("on_detail_action_triggered")
