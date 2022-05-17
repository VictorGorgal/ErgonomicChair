from PyQt6.QtCore import QPropertyAnimation
from front_end.UI_base import Ui_MainWindow
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.page_widgets.setCurrentWidget(self.home_page)  # starts on home page

        self.btn_menu.clicked.connect(lambda: self.toggleMenu(48))  # slide menu

        self.btn_home.clicked.connect(lambda: self.page_widgets.setCurrentWidget(self.home_page))  # change pages
        self.btn_graphs.clicked.connect(lambda: self.page_widgets.setCurrentWidget(self.graph_page))
        self.btn_conect.clicked.connect(lambda: self.page_widgets.setCurrentWidget(self.connection_page))
        self.btn_config.clicked.connect(lambda: self.page_widgets.setCurrentWidget(self.config_page))

    def toggleMenu(self, maxWidth):
        width = self.slide_menu.width()
        standard = 0  # minimum width
        widthExtended = standard

        if width == standard:
            widthExtended = maxWidth

        # ANIMATION
        self.animation = QPropertyAnimation(self.slide_menu, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()


if __name__ == '__main__':
    import sys

    app = qtw.QApplication([])

    MainWindow = MainWindow()
    MainWindow.show()

    sys.exit(app.exec())
