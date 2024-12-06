#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书组件

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-12-02
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from qfluentwidgets import (
    CardWidget,
    CaptionLabel,
    StrongBodyLabel,
    FluentIcon,
    PushButton,
    TransparentToolButton,
)
from src.common.signal_bus import signalBus
from src.components.network_image_viewer import NetworkImageViewer
from src.views.novel.data_class.explore import DataExplore
from src.views.novel.data_class.source import RuleSource


class BookCard(CardWidget):
    def __init__(
        self, parent=None, data: DataExplore = None, source: RuleSource = None
    ) -> None:
        super().__init__(parent)
        self.data = data
        self.source = source
        # print(data)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        grid_form_layout = QGridLayout(self)
        widget_body = QWidget(self)
        grid_body_layout = QGridLayout(widget_body)

        cover_viewer = NetworkImageViewer(widget_body)
        cover_viewer.setFixedSize(90, 120)
        cover_url = getattr(data, "cover_url", None)
        if cover_url:
            # if not cover_url.startswith("http"):
            #     source_url = source.get("source_url")
            #     url = urljoin(source_url, cover_url)
            # else:
            #     url = cover_url
            # cover_viewer.load_image(url)
            cover_viewer.load_image("src/resource/images/nocover.jpg")
        else:
            cover_viewer.load_image("src/resource/images/nocover.jpg")
        grid_body_layout.addWidget(cover_viewer, 0, 0, 1, 1)

        wgt_detail = QWidget(widget_body)
        grid_detail = QGridLayout(wgt_detail)
        grid_body_layout.addWidget(wgt_detail, 0, 1, 1, 1)

        title_label = StrongBodyLabel("无", self)
        if getattr(data, "name", None):
            if len(getattr(data, "name")) > 25:
                title_label.setText(f'{getattr(data, 'name')[:25]}...')
            else:
                title_label.setText(getattr(data, "name"))
        author_label = CaptionLabel("无", self)
        if getattr(data, "author"):
            author_label.setText(getattr(data, "author"))
        intro_text = getattr(data, "intro", "")
        intro_label = QLabel(intro_text)
        intro_label.setWordWrap(True)
        grid_detail.addWidget(title_label, 0, 0, 1, 1)
        grid_detail.addWidget(author_label, 1, 0, 1, 1)
        grid_detail.addWidget(intro_label, 2, 0, 1, 1)

        grid_form_layout.addWidget(widget_body, 0, 0, 1, 1)

        self.read_btn = PushButton("阅读", self)
        more_btn = TransparentToolButton(FluentIcon.MORE, self)
        more_btn.setFixedSize(32, 32)
        wgt_btn = QWidget(widget_body)
        wgt_btn.setMaximumWidth(140)
        grid_btn = QGridLayout(wgt_btn)
        grid_btn.addWidget(self.read_btn, 0, 0, 1, 1)
        grid_btn.addWidget(more_btn, 0, 1, 1, 1)

        grid_form_layout.addWidget(wgt_btn, 0, 1, 1, 1)
        self.setFixedHeight(150)

        self.init_signal()

    def init_signal(self):
        self.read_btn.clicked.connect(self.on_read_triggered)

    def on_read_triggered(self):
        print("on_read_action_triggered")
        signalBus.novel_change_page.emit("content")
        signalBus.novel_rule_source.emit(self.source)
        signalBus.novel_bool_url.emit(self.data)

    def on_detail_triggered(self):
        print("on_detail_action_triggered")
