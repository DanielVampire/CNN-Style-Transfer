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
        label = GoodQLabel(self)
        label.clicked.connect(self.EventForLable)
        pix=QtGui.QPixmap(self.Images[len(self.Images)-1][0])
        label.setPixmap(pix.scaled(140,140))
        self.ImageLayout.addWidget(label)
        self.Labels.append(label)
        self.TakePic.setEnabled(False)
    def TakeStyleImages(self):
        self.Styles.append(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение стиль",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
        label = GoodQLabel(self)
        self.ImageLayout.addWidget(label)
        label.clicked.connect(self.EventForLable)
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
        sender = self.sender()
        for i in self.Labels:
            if sender == i:
                i.parent=None
                i.deleteLater()
                self.update()

    def AddPictures(self):
        self.CountStyleinImages.append([len(self.Images),len(self.Styles)])
        self.TakePic.setEnabled(True)

class GoodQLabel(QtWidgets.QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        QtWidgets.QLabel.__init__(parent=parent, flags=flags)

    def mouseDoubleClickEvent(self,event):
        self.clicked.emit()