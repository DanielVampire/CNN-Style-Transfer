# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\CreatingProg\Neural Network\CNN Style Transfer\CNN Style Transfer\UI_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.TabPics = QtWidgets.QTabWidget(Dialog)
        self.TabPics.setGeometry(QtCore.QRect(10, 50, 381, 201))
        self.TabPics.setTabPosition(QtWidgets.QTabWidget.North)
        self.TabPics.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.TabPics.setElideMode(QtCore.Qt.ElideNone)
        self.TabPics.setDocumentMode(False)
        self.TabPics.setMovable(False)
        self.TabPics.setTabBarAutoHide(False)
        self.TabPics.setObjectName("TabPics")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 381, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TakePic = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.TakePic.setGeometry(QtCore.QRect(30, 20, 311, 23))
        self.TakePic.setObjectName("TakePic")
        self.TakeStyle = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.TakeStyle.setGeometry(QtCore.QRect(30, 70, 311, 23))
        self.TakeStyle.setObjectName("TakeStyle")
        self.AddStyle = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.AddStyle.setGeometry(QtCore.QRect(170, 110, 31, 23))
        self.AddStyle.setObjectName("AddStyle")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.TabPics.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TabPics.addTab(self.tab_2, "")
        self.UsePics = QtWidgets.QPushButton(Dialog)
        self.UsePics.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.UsePics.setObjectName("UsePics")
        self.AddPic = QtWidgets.QPushButton(Dialog)
        self.AddPic.setGeometry(QtCore.QRect(130, 10, 141, 23))
        self.AddPic.setObjectName("AddPic")

        self.retranslateUi(Dialog)
        self.TabPics.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TakePic.setText(_translate("Dialog", "Выберите изображение"))
        self.TakeStyle.setText(_translate("Dialog", "Выберите стиль"))
        self.AddStyle.setText(_translate("Dialog", "+"))
        self.TabPics.setTabText(self.TabPics.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.UsePics.setText(_translate("Dialog", "Выбрать"))
        self.AddPic.setText(_translate("Dialog", "Добавить изображение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
