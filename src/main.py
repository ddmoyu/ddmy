# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from views.view import MainWindow
from qfluentwidgets import setTheme, Theme

if __name__ == '__main__':
    setTheme(Theme.DARK)
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()