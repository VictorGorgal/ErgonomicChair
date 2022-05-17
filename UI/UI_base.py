# Form implementation generated from reading ui file 'UI_base.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 614)
        MainWindow.setStyleSheet("background-color: rgb(24,24,29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 32))
        self.top_bar.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.top_bar.setLineWidth(0)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_menu = QtWidgets.QFrame(self.top_bar)
        self.toggle_menu.setMaximumSize(QtCore.QSize(70, 32))
        self.toggle_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.toggle_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.toggle_menu.setLineWidth(0)
        self.toggle_menu.setObjectName("toggle_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.toggle_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_menu.setMaximumSize(QtCore.QSize(45, 32))
        self.btn_menu.setStyleSheet("QPushButton:pressed {\n"
"    border-style: inset;\n"
"}")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/menu-b.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_menu.setAutoDefault(False)
        self.btn_menu.setDefault(False)
        self.btn_menu.setFlat(True)
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.horizontalLayout.addWidget(self.toggle_menu)
        self.frame = QtWidgets.QFrame(self.top_bar)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.content.setLineWidth(0)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.content)
        self.slide_menu.setMinimumSize(QtCore.QSize(0, 300))
        self.slide_menu.setMaximumSize(QtCore.QSize(0, 1000))
        self.slide_menu.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.slide_menu.setLineWidth(0)
        self.slide_menu.setObjectName("slide_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.slide_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icons_frame = QtWidgets.QFrame(self.slide_menu)
        self.icons_frame.setMinimumSize(QtCore.QSize(0, 300))
        self.icons_frame.setMaximumSize(QtCore.QSize(46, 1000))
        self.icons_frame.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.icons_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.icons_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.icons_frame.setLineWidth(0)
        self.icons_frame.setObjectName("icons_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icons_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_home = QtWidgets.QPushButton(self.icons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: inset;\n"
"}")
        self.btn_home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/c1-b4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QtCore.QSize(32, 32))
        self.btn_home.setAutoDefault(False)
        self.btn_home.setDefault(False)
        self.btn_home.setFlat(True)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)
        self.btn_graphs = QtWidgets.QPushButton(self.icons_frame)
        self.btn_graphs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_graphs.sizePolicy().hasHeightForWidth())
        self.btn_graphs.setSizePolicy(sizePolicy)
        self.btn_graphs.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_graphs.setAutoFillBackground(False)
        self.btn_graphs.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: inset;\n"
"}")
        self.btn_graphs.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/c2-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_graphs.setIcon(icon2)
        self.btn_graphs.setIconSize(QtCore.QSize(32, 32))
        self.btn_graphs.setFlat(True)
        self.btn_graphs.setObjectName("btn_graphs")
        self.verticalLayout_4.addWidget(self.btn_graphs)
        self.btn_conect = QtWidgets.QPushButton(self.icons_frame)
        self.btn_conect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_conect.sizePolicy().hasHeightForWidth())
        self.btn_conect.setSizePolicy(sizePolicy)
        self.btn_conect.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_conect.setAutoFillBackground(False)
        self.btn_conect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: inset;\n"
"}")
        self.btn_conect.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/c3-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_conect.setIcon(icon3)
        self.btn_conect.setIconSize(QtCore.QSize(32, 32))
        self.btn_conect.setFlat(True)
        self.btn_conect.setObjectName("btn_conect")
        self.verticalLayout_4.addWidget(self.btn_conect)
        self.btn_config = QtWidgets.QPushButton(self.icons_frame)
        self.btn_config.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_config.setAutoFillBackground(False)
        self.btn_config.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: inset;\n"
"}")
        self.btn_config.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/c4-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_config.setIcon(icon4)
        self.btn_config.setIconSize(QtCore.QSize(32, 32))
        self.btn_config.setFlat(True)
        self.btn_config.setObjectName("btn_config")
        self.verticalLayout_4.addWidget(self.btn_config)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.icons_frame)
        self.horizontalLayout_2.addWidget(self.slide_menu)
        self.frame_3 = QtWidgets.QFrame(self.content)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 2))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.page_widgets = QtWidgets.QStackedWidget(self.frame_3)
        self.page_widgets.setEnabled(True)
        self.page_widgets.setAutoFillBackground(False)
        self.page_widgets.setLineWidth(0)
        self.page_widgets.setObjectName("page_widgets")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.label = QtWidgets.QLabel(self.home_page)
        self.label.setGeometry(QtCore.QRect(420, 40, 191, 41))
        self.label.setObjectName("label")
        self.page_widgets.addWidget(self.home_page)
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.label_2 = QtWidgets.QLabel(self.graph_page)
        self.label_2.setGeometry(QtCore.QRect(200, 270, 151, 71))
        self.label_2.setObjectName("label_2")
        self.page_widgets.addWidget(self.graph_page)
        self.connection_page = QtWidgets.QWidget()
        self.connection_page.setObjectName("connection_page")
        self.label_3 = QtWidgets.QLabel(self.connection_page)
        self.label_3.setGeometry(QtCore.QRect(670, 290, 211, 71))
        self.label_3.setObjectName("label_3")
        self.page_widgets.addWidget(self.connection_page)
        self.config_page = QtWidgets.QWidget()
        self.config_page.setObjectName("config_page")
        self.label_5 = QtWidgets.QLabel(self.config_page)
        self.label_5.setGeometry(QtCore.QRect(690, 190, 211, 91))
        self.label_5.setObjectName("label_5")
        self.page_widgets.addWidget(self.config_page)
        self.verticalLayout_3.addWidget(self.page_widgets)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.page_widgets.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "Graph"))
        self.label_3.setText(_translate("MainWindow", "Connections"))
        self.label_5.setText(_translate("MainWindow", "Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())