# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 692)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(50, 50, 50, 255));\n"
"}\n"
"QMenuBar{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(50, 50, 50, 255));\n"
"    font: 75 10pt \"Segoe Script\";\n"
"}\n"
"QMenu{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(50, 50, 50, 255));\n"
"    font: 75 10pt \"Segoe Script\";\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setMaximumSize(QtCore.QSize(1920, 980))
        self.Image.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Segoe Script\";\n"
"}")
        self.Image.setTextFormat(QtCore.Qt.AutoText)
        self.Image.setScaledContents(False)
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.verticalLayout.addWidget(self.Image)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ImagesTake = QtWidgets.QPushButton(self.centralwidget)
        self.ImagesTake.setMaximumSize(QtCore.QSize(410, 50))
        self.ImagesTake.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImagesTake.setStyleSheet("QPushButton{\n"
"    font: 24pt \"Segoe Script\";\n"
"    text-decoration: underline;\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 157, 0);\n"
"}\n"
"")
        self.ImagesTake.setAutoDefault(False)
        self.ImagesTake.setDefault(False)
        self.ImagesTake.setFlat(False)
        self.ImagesTake.setObjectName("ImagesTake")
        self.horizontalLayout_2.addWidget(self.ImagesTake)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(1, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setStyleSheet("QFrame{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(50, 50, 50, 255));\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, -1, -1, 9)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.CancelButton = QtWidgets.QPushButton(self.frame)
        self.CancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CancelButton.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.NumStepsLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.NumStepsLabel.setFont(font)
        self.NumStepsLabel.setStyleSheet("QFrame{\n"
"    \n"
"    font: 75 14pt \"Segoe Script\";\n"
"    color:rgb(0, 0, 0);\n"
"    background: rgba(255, 255, 255, 0);\n"
"}")
        self.NumStepsLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NumStepsLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NumStepsLabel.setLineWidth(3)
        self.NumStepsLabel.setMidLineWidth(0)
        self.NumStepsLabel.setTextFormat(QtCore.Qt.AutoText)
        self.NumStepsLabel.setWordWrap(False)
        self.NumStepsLabel.setIndent(-1)
        self.NumStepsLabel.setOpenExternalLinks(False)
        self.NumStepsLabel.setObjectName("NumStepsLabel")
        self.horizontalLayout.addWidget(self.NumStepsLabel)
        self.NumStepsBox = QtWidgets.QSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.NumStepsBox.setFont(font)
        self.NumStepsBox.setStyleSheet("QSpinBox{\n"
"    font: 75 14pt \"Segoe Script\";\n"
"    color: rgb(0, 0, 0);\n"
"    background: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.NumStepsBox.setMinimum(1)
        self.NumStepsBox.setMaximum(9999)
        self.NumStepsBox.setProperty("value", 1)
        self.NumStepsBox.setObjectName("NumStepsBox")
        self.horizontalLayout.addWidget(self.NumStepsBox)
        self.NumStepButton = QtWidgets.QPushButton(self.frame)
        self.NumStepButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NumStepButton.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.NumStepButton.setObjectName("NumStepButton")
        self.horizontalLayout.addWidget(self.NumStepButton)
        self.SaveImageButton = QtWidgets.QPushButton(self.frame)
        self.SaveImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveImageButton.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.SaveImageButton.setObjectName("SaveImageButton")
        self.horizontalLayout.addWidget(self.SaveImageButton)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.TakeImage = QtWidgets.QAction(MainWindow)
        self.TakeImage.setCheckable(False)
        self.TakeImage.setChecked(False)
        self.TakeImage.setObjectName("TakeImage")
        self.SaveImage = QtWidgets.QAction(MainWindow)
        self.SaveImage.setObjectName("SaveImage")
        self.ExitMenu = QtWidgets.QAction(MainWindow)
        self.ExitMenu.setCheckable(False)
        self.ExitMenu.setObjectName("ExitMenu")
        self.Ref = QtWidgets.QAction(MainWindow)
        self.Ref.setObjectName("Ref")
        self.HelpBut = QtWidgets.QAction(MainWindow)
        self.HelpBut.setObjectName("HelpBut")
        self.menu.addAction(self.TakeImage)
        self.menu.addAction(self.ExitMenu)
        self.menu_2.addAction(self.Ref)
        self.menu_2.addAction(self.HelpBut)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Neural Style Transfer"))
        self.Image.setText(_translate("MainWindow", "Добро пожаловать\n"
" Для того, чтобы начать работу выберите изображения\n"
"Нажав кнопку ниже"))
        self.ImagesTake.setText(_translate("MainWindow", "Выбрать изображения"))
        self.ExitButton.setText(_translate("MainWindow", "Выйти"))
        self.CancelButton.setText(_translate("MainWindow", "Не сохранять"))
        self.NumStepsLabel.setText(_translate("MainWindow", "Укажите степень смешивания"))
        self.NumStepButton.setText(_translate("MainWindow", "Применить"))
        self.SaveImageButton.setText(_translate("MainWindow", "Сохранить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.TakeImage.setText(_translate("MainWindow", "Выбрать изображение"))
        self.SaveImage.setText(_translate("MainWindow", "Сохранить"))
        self.ExitMenu.setText(_translate("MainWindow", "Выход"))
        self.Ref.setText(_translate("MainWindow", "Справка"))
        self.HelpBut.setText(_translate("MainWindow", "Помощь"))
