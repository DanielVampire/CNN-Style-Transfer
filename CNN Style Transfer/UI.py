# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\CreatingProg\Neural Network\CNN Style Transfer\CNN Style Transfer\UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 614)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(620, 0, 181, 571))
        self.frame.setStyleSheet("background:rgb(255, 255, 255) ")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.AvtoRadioButton = QtWidgets.QRadioButton(self.frame)
        self.AvtoRadioButton.setGeometry(QtCore.QRect(40, 50, 111, 17))
        self.AvtoRadioButton.setCheckable(True)
        self.AvtoRadioButton.setChecked(False)
        self.AvtoRadioButton.setAutoRepeat(False)
        self.AvtoRadioButton.setObjectName("AvtoRadioButton")
        self.ManualRadioButton = QtWidgets.QRadioButton(self.frame)
        self.ManualRadioButton.setGeometry(QtCore.QRect(40, 80, 82, 17))
        self.ManualRadioButton.setObjectName("ManualRadioButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 101, 21))
        self.label.setObjectName("label")
        self.AvtoBox = QtWidgets.QGroupBox(self.frame)
        self.AvtoBox.setGeometry(QtCore.QRect(10, 50, 161, 101))
        self.AvtoBox.setToolTip("")
        self.AvtoBox.setToolTipDuration(-1)
        self.AvtoBox.setWhatsThis("")
        self.AvtoBox.setObjectName("AvtoBox")
        self.label_2 = QtWidgets.QLabel(self.AvtoBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.NumStepsAvto = QtWidgets.QLineEdit(self.AvtoBox)
        self.NumStepsAvto.setGeometry(QtCore.QRect(90, 30, 61, 20))
        self.NumStepsAvto.setObjectName("NumStepsAvto")
        self.AvtoBoxButton = QtWidgets.QPushButton(self.AvtoBox)
        self.AvtoBoxButton.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.AvtoBoxButton.setObjectName("AvtoBoxButton")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 460, 801, 121))
        self.frame_2.setStyleSheet("background: rgb(255, 255, 255);\n"
"QPushButton\n"
"{\n"
"    height: 30;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ReturnBackButton = QtWidgets.QPushButton(self.frame_2)
        self.ReturnBackButton.setGeometry(QtCore.QRect(20, 20, 181, 81))
        self.ReturnBackButton.setStyleSheet("background: rgb(85, 255, 127)")
        self.ReturnBackButton.setObjectName("ReturnBackButton")
        self.SaveImageButton = QtWidgets.QPushButton(self.frame_2)
        self.SaveImageButton.setGeometry(QtCore.QRect(650, 20, 131, 81))
        self.SaveImageButton.setStyleSheet("background: rgb(85, 255, 127)")
        self.SaveImageButton.setObjectName("SaveImageButton")
        self.OneStepButton = QtWidgets.QPushButton(self.frame_2)
        self.OneStepButton.setGeometry(QtCore.QRect(220, 20, 191, 38))
        self.OneStepButton.setStyleSheet("QPushButton\n"
"{\n"
"    background: rgb(147, 167, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background:rgb(255, 0, 0)\n"
"}")
        self.OneStepButton.setObjectName("OneStepButton")
        self.TenStepButton = QtWidgets.QPushButton(self.frame_2)
        self.TenStepButton.setGeometry(QtCore.QRect(420, 20, 190, 38))
        self.TenStepButton.setStyleSheet("QPushButton\n"
"{\n"
"    background: rgb(147, 167, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background:rgb(255, 0, 0)\n"
"}")
        self.TenStepButton.setObjectName("TenStepButton")
        self.HundredStepButton = QtWidgets.QPushButton(self.frame_2)
        self.HundredStepButton.setGeometry(QtCore.QRect(220, 60, 191, 38))
        self.HundredStepButton.setStyleSheet("QPushButton\n"
"{\n"
"    background: rgb(147, 167, 255)\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background:rgb(255, 0, 0)\n"
"}")
        self.HundredStepButton.setObjectName("HundredStepButton")
        self.ThousandStepButton = QtWidgets.QPushButton(self.frame_2)
        self.ThousandStepButton.setGeometry(QtCore.QRect(420, 60, 190, 38))
        self.ThousandStepButton.setStyleSheet("background: rgb(147, 167, 255)")
        self.ThousandStepButton.setObjectName("ThousandStepButton")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(240, 200, 47, 13))
        self.Image.setObjectName("Image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.TakeImage = QtWidgets.QAction(MainWindow)
        self.TakeImage.setObjectName("TakeImage")
        self.SaveImage = QtWidgets.QAction(MainWindow)
        self.SaveImage.setObjectName("SaveImage")
        self.ExitMenu = QtWidgets.QAction(MainWindow)
        self.ExitMenu.setObjectName("ExitMenu")
        self.Help = QtWidgets.QAction(MainWindow)
        self.Help.setObjectName("Help")
        self.Education = QtWidgets.QAction(MainWindow)
        self.Education.setObjectName("Education")
        self.menu.addAction(self.TakeImage)
        self.menu.addAction(self.SaveImage)
        self.menu.addAction(self.ExitMenu)
        self.menu_2.addAction(self.Help)
        self.menu_2.addAction(self.Education)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AvtoRadioButton.setText(_translate("MainWindow", "Автоматический"))
        self.ManualRadioButton.setText(_translate("MainWindow", "Ручной"))
        self.label.setText(_translate("MainWindow", "Выберите режим"))
        self.AvtoBox.setStatusTip(_translate("MainWindow", "Окошечко автоматического режима работы программы"))
        self.AvtoBox.setTitle(_translate("MainWindow", "Автоматический"))
        self.label_2.setText(_translate("MainWindow", "Кол-во шагов :"))
        self.AvtoBoxButton.setText(_translate("MainWindow", "Применить"))
        self.ReturnBackButton.setText(_translate("MainWindow", "Вернуться на шаг назад"))
        self.SaveImageButton.setText(_translate("MainWindow", "Сохранить"))
        self.OneStepButton.setText(_translate("MainWindow", "1 шаг"))
        self.TenStepButton.setText(_translate("MainWindow", "10 шагов"))
        self.HundredStepButton.setText(_translate("MainWindow", "100 шагов"))
        self.ThousandStepButton.setText(_translate("MainWindow", "1000 шагов"))
        self.Image.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Помощь"))
        self.TakeImage.setText(_translate("MainWindow", "Выбрать изображение"))
        self.SaveImage.setText(_translate("MainWindow", "Сохранить"))
        self.ExitMenu.setText(_translate("MainWindow", "Выход"))
        self.Help.setText(_translate("MainWindow", "Справка"))
        self.Education.setText(_translate("MainWindow", "Обучение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
