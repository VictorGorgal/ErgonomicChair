from PyQt6.QtCore import QPropertyAnimation
from UI.UI_base import Ui_MainWindow
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.page_widgets.setCurrentWidget(self.home_page)  # starts on home page
        self.slide_menu.setMaximumWidth(0)

        self.btn_menu.clicked.connect(lambda: self.toggleMenu(48))  # slide menu

        self.btn_home.clicked.connect(self.home_btn_func)  # side buttons
        self.btn_graphs.clicked.connect(self.graphs_btn_func)
        self.btn_connect.clicked.connect(self.connect_btn_func)
        self.btn_config.clicked.connect(self.config_btn_func)

        self.highlight_button()

    def home_btn_func(self):
        self.page_widgets.setCurrentWidget(self.home_page)
        self.highlight_button()

    def graphs_btn_func(self):
        self.page_widgets.setCurrentWidget(self.graph_page)
        self.highlight_button()

    def connect_btn_func(self):
        self.page_widgets.setCurrentWidget(self.connection_page)
        self.highlight_button()

    def config_btn_func(self):
        self.page_widgets.setCurrentWidget(self.config_page)
        self.highlight_button()

    def highlight_button(self):
        self.btn_home.setAutoFillBackground(False)
        self.btn_graphs.setAutoFillBackground(False)
        self.btn_connect.setAutoFillBackground(False)
        self.btn_config.setAutoFillBackground(False)

        if self.page_widgets.currentWidget().objectName() == 'home_page':
            self.btn_home.setAutoFillBackground(True)
        if self.page_widgets.currentWidget().objectName() == 'graph_page':
            self.btn_graphs.setAutoFillBackground(True)
        if self.page_widgets.currentWidget().objectName() == 'connection_page':
            self.btn_connect.setAutoFillBackground(True)
        if self.page_widgets.currentWidget().objectName() == 'config_page':
            self.btn_config.setAutoFillBackground(True)

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

        self.highlight_button()


if __name__ == '__main__':
    import sys

    app = qtw.QApplication([])

    MainWindow = MainWindow()
    MainWindow.show()

    sys.exit(app.exec())
