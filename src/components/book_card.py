#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
书组件

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-12-02
"""
from typing import Any
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QGridLayout, QWidget
from qfluentwidgets import (
    CardWidget,
    CaptionLabel,
    StrongBodyLabel,
    FluentIcon,
    PushButton,
    TransparentToolButton,
)
from src.components.network_image_viewer import NetworkImageViewer


class BookCard(CardWidget):
    book_clicked = Signal(dict)

    def __init__(self, parent=None, book_data: Any=None, source: Any = None) -> None:
        super().__init__(parent)
        self.book_data = book_data
        # print(book_data)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        grid_form_layout = QGridLayout(self)
        widget_body = QWidget(self)
        grid_body_layout = QGridLayout(widget_body)

        cover_viewer = NetworkImageViewer(widget_body)
        cover_viewer.setFixedSize(90, 120)
        cover_url = getattr(book_data, 'cover_url', None)
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
        if getattr(book_data, 'name', None):
            if len(getattr(book_data, 'name')) > 25:
                title_label.setText(f'{getattr(book_data, 'name')[:25]}...')
            else:
                title_label.setText(getattr(book_data, 'name'))
        author_label = CaptionLabel("无", self)
        if getattr(book_data, 'author'):
            author_label.setText(getattr(book_data, 'author'))
        intro_text = getattr(book_data, 'intro', "")
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
