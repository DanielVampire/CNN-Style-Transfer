import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic
import functools

dialogForm = uic.loadUiType("UI_Dialog.ui")[0]

class Dialog(QtWidgets.QDialog, dialogForm):
    def __init__(self):
        QtWidgets.QDialog.__init__(self,None)
        self.setupUi(self)
        self.Images=[]
        self.TakePic.clicked.connect(self.TakePicture)
        self.TakeStyle.clicked.connect(self.TakeStyleImages)
        self.AddPic.clicked.connect(self.AddPictures)
        self.TakeStyle.setEnabled(False)
        self.labstyle.setVisible(False)
        self.labizo.setVisible(False)
        self.ImageCounter = 0
    def resizeEvent(self,event):
        event.accept()
    def TakePicture(self):
        t= list(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
        t.pop(1)
        self.Images.append(t)
        self.TakeStyle.setEnabled(True)
        self.TakePic.setEnabled(False)
    def TakeStyleImages(self):
        for i in self.Images:
            if (len(self.Images)-1) == self.Images.index(i):
                t= list(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение стиль",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
                t.pop(1)
                t=str(t[0])
                i.append(t)
                break
    def ShowImages(self):
        Hlayout = QtWidgets.QHBoxLayout(self)
        self.labstyle.setVisible(True)
        self.labizo.setVisible(True)
        Button = QtWidgets.QPushButton(self)
        Button.setText("X")
        Button.setMinimumSize(30,140)
        Button.clicked.connect(lambda checked : self.DeleteImages( checked, Hlayout) )
        for i in range(self.ImageCounter, len(self.Images)):
            for j in self.Images[i]:
                Image = QtWidgets.QLabel(self)
                pix = QtGui.QPixmap(j)
                Image.setPixmap(pix.scaled(140,140))
                Hlayout.addWidget(Image)
                per = self.Images[i]
                if per.index(j) == 0:
                    text = QtWidgets.QLabel(j)
                    text.setVisible(False)
                    Hlayout.addWidget(text)
        self.ImageCounter+=1
        Hlayout.addWidget(Button)
        self.ImageShow.addLayout(Hlayout)
    def DeleteImages(self,checked,Layout):
        for i in range(self.ImageShow.count()):
            obj = self.ImageShow.itemAt(i)
            if obj == Layout:
                rest = True
                while rest:
                    if Layout.count() == 0:
                        break
                    for iterate in range(Layout.count()):
                        widget = Layout.itemAt(iterate).widget()
                        if widget is None:
                            rest=False
                            break
                        for image in self.Images:
                            if widget.text() == image[0]:
                                self.Images.remove(image)
                                break
                        Layout.removeWidget(widget)
                        widget.deleteLater()
                        widget = None
                        break
                self.ImageShow.removeItem(obj)
                self.ImageShow.update()
                break
        if self.ImageShow.count() == 1:
            obj = self.ImageShow.itemAt(0)
            labI = obj.itemAt(0).widget()
            labS = obj.itemAt(1).widget()
            labI.setVisible(False)
            labS.setVisible(False)
        self.ImageCounter=0
    def EventForLableImages(self, VLayout,event):
        restart=True
        while restart:
            print(self.ImageLayout.count())
            if self.ImageLayout.count() == 0:
                restart=False
            for j in range(self.ImageLayout.count()):
                obj = self.ImageLayout.takeAt(j)
                print(obj.widget())
                if obj == None:
                    restart=False
                    break
                if obj == VLayout:
                    for i in self.Images:
                        elem = obj.takeAt(1).widget()
                        if i[0] == elem.text():
                            self.ImageLayout.removeItem(obj)
                            self.Images.remove(i)
                            print(self.ImageLayout.count())
                            break
                    break
                elif type(obj.widget()) == type(QtWidgets.QLabel()):
                    self.ImageLayout.removeItem(obj)
                    break
                elif type(obj) == type(QtWidgets.QVBoxLayout()):
                    restart = False
                    break
        self.update()
                
    def EventForLableStyles(self, VLayout,event):
        lb_1 = VLayout.children[0]
        lb_2 = VLayout.children[1]
        self.Labels.remove(lb_1)
        lb_1.deleteLater()

    def AddPictures(self):
        self.TakePic.setEnabled(True)
        self.TakeStyle.setEnabled(False)
        self.ShowImages()
