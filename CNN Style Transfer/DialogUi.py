# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(536, 515)
        Dialog.setStyleSheet("QWidget{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 50, 50, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Grid = QtWidgets.QGridLayout()
        self.Grid.setContentsMargins(-1, 0, 0, 0)
        self.Grid.setHorizontalSpacing(6)
        self.Grid.setObjectName("Grid")
        self.AddPic = QtWidgets.QPushButton(Dialog)
        self.AddPic.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(0, 0, 0);\n"
"    border: 1px;\n"
"    background: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.AddPic.setObjectName("AddPic")
        self.Grid.addWidget(self.AddPic, 0, 0, 1, 1)
        self.UsePics = QtWidgets.QPushButton(Dialog)
        self.UsePics.setStatusTip("")
        self.UsePics.setWhatsThis("")
        self.UsePics.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(227, 0, 3);\n"
"    border: 1px;\n"
"    background: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.UsePics.setObjectName("UsePics")
        self.Grid.addWidget(self.UsePics, 3, 0, 1, 1)
        self.TakeStyle = QtWidgets.QPushButton(Dialog)
        self.TakeStyle.setEnabled(True)
        self.TakeStyle.setStyleSheet("QPushButton{\n"
"    font: 16pt \"Segoe Script\";\n"
"    color:  rgb(0, 0, 0);\n"
"    border: 1px;\n"
"    background: rgba(255, 255, 255,0);\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"    color: rgb(0, 157, 0);\n"
"}")
        self.TakeStyle.setObjectName("TakeStyle")
        self.Grid.addWidget(self.TakeStyle, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.Grid, 1, 1, 1, 1)
        self.ImageShow = QtWidgets.QVBoxLayout()
        self.ImageShow.setObjectName("ImageShow")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labizo = QtWidgets.QLabel(Dialog)
        self.labizo.setStyleSheet("font: 75 14pt \"Segoe Script\";\n"
"background: rgba(255, 255, 255,0);")
        self.labizo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labizo.setIndent(0)
        self.labizo.setObjectName("labizo")
        self.horizontalLayout_2.addWidget(self.labizo)
        self.labstyle = QtWidgets.QLabel(Dialog)
        self.labstyle.setStyleSheet("font: 75 14pt \"Segoe Script\";\n"
"background: rgba(255, 255, 255,0);")
        self.labstyle.setAlignment(QtCore.Qt.AlignCenter)
        self.labstyle.setObjectName("labstyle")
        self.horizontalLayout_2.addWidget(self.labstyle)
        self.ImageShow.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.ImageShow, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choose Images"))
        self.AddPic.setText(_translate("Dialog", "Добавить изображение"))
        self.UsePics.setText(_translate("Dialog", "Применить"))
        self.TakeStyle.setText(_translate("Dialog", "Добавить стили"))
        self.labizo.setText(_translate("Dialog", "Изображения"))
        self.labstyle.setText(_translate("Dialog", "Стили"))
