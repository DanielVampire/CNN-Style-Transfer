import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

dialogForm = uic.loadUiType("UI_Dialog.ui")[0]

class Dialog(QtWidgets.QDialog, dialogForm):
    def __init__(self):
        QtWidgets.QDialog.__init__(self,None)
        self.setupUi(self)
        self.Images=[]
        self.Styles=[]
        self.Labels=[]
        self.CountStyleinImages=[]
        self.TakePic.clicked.connect(self.TakePicture)
        self.TakeStyle.clicked.connect(self.TakeStyleImages)
        self.AddPic.clicked.connect(self.AddPictures)
    def resizeEvent(self,event):
        event.accept()
    def TakePicture(self):
        self.Images.append(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
        label = QtWidgets.QLabel(self)
        label.mouseDoubleClickEvent=self.EventForLable
        pix=QtGui.QPixmap(self.Images[len(self.Images)-1][0])
        label.setPixmap(pix.scaled(140,140))
        self.ImageLayout.addWidget(label)
        self.Labels.append(label)
        self.TakePic.setEnabled(False)
    def TakeStyleImages(self):
        self.Styles.append(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение стиль",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
        label = QtWidgets.QLabel(self)
        self.ImageLayout.addWidget(label)
        label.mouseDoubleClickEvent=self.EventForLable
        pix=QtGui.QPixmap(self.Styles[len(self.Styles)-1][0])
        label.setPixmap(pix.scaled(140,140))
        emptyPix = QtGui.QPixmap(140,140)
        emptyPix.fill(QtCore.Qt.white)
        baglabel = QtWidgets.QLabel(self)
        baglabel.setPixmap(emptyPix)

        self.StyleLayout.addWidget(label)
        if self.StyleLayout.count() > self.ImageLayout.count():
            self.ImageLayout.addWidget(baglabel)
        self.Labels.append(label)
    
    def EventForLable(self,event):
        print(self.sender().text())
    def AddPictures(self):
        self.CountStyleinImages.append([len(self.Images),len(self.Styles)])
        self.TakePic.setEnabled(True)