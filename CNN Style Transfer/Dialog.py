import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic
import functools

dialogForm = uic.loadUiType("UI_Dialog.ui")[0]

class Dialog(QtWidgets.QWidget, dialogForm):
    def __init__(self,parent = None):
        super().__init__(parent,QtCore.Qt.Window)
        self.setupUi(self)
        self.Images=[]
        self.LayoutImages = None
        self.TakeStyle.clicked.connect(self.TakeStyleImages)
        self.AddPic.clicked.connect(self.TakePicture)
        self.UsePics.clicked.connect(self.DragImageToMW)
        self.TakeStyle.setEnabled(False)
        self.AddPic.setEnabled(True)
        self.labstyle.setVisible(False)
        self.labizo.setVisible(False)
        self.UsePics.setEnabled(False)

        self.ImageSize = None
        self.StyleSize = None
        self.ImageCounter = 0
        self.StyleCounter = 1

    def DragImageToMW(self):
        self.parent().Images=self.Images
        self.parent().ConfirmMode()
        self.close()

    def TakePicture(self):
        t= list(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
        if t[0] == "":
            QtWidgets.QMessageBox.warning(self,"Предупреждение","Необходимо выбрать изображение")
            return
        t.pop(1)
        self.Images.append(t)
        self.TakeStyle.setEnabled(True)
        self.ShowImage()
        self.AddPic.setEnabled(False)

    def TakeStyleImages(self):
        for i in self.Images:
            if (len(self.Images)-1) == self.Images.index(i):
                t= list(QtWidgets.QFileDialog.getOpenFileName(None,"Укажите изображение стиль",QtCore.QDir.homePath(),"Файл изображения (*.jpg);;Все файлы (*.*)"))
                if t[0] == "":
                    QtWidgets.QMessageBox.warning(self,"Предупреждение","Необходимо выбрать изображение")
                    return
                t.pop(1)
                t=str(t[0])
                i.append(t)
                break
        self.UsePics.setEnabled(True)
        self.ShowStyle()
        self.AddPic.setEnabled(True)
    
    def ShowImage(self):
        if self.ImageShow.count() > 1:
            Button = QtWidgets.QPushButton(self)
            Button.setText("X")
            Button.setMinimumSize(30,140)
            Button.setMaximumSize(30,140)
            HLayout = self.LayoutImages
            Button.clicked.connect(lambda checked : self.DeleteImages( checked, HLayout) )
            self.LayoutImages.addWidget(Button)
            self.ImageCounter+=1
        self.LayoutImages = QtWidgets.QHBoxLayout(self)
        self.labstyle.setVisible(True)
        self.labizo.setVisible(True)
        for i in range(self.ImageCounter, len(self.Images)):
            Image = QtWidgets.QLabel(self)
            pix = QtGui.QPixmap(self.Images[i][0])
            self.ImageSize = pix.size()
            Image.setPixmap(pix.scaled(140,140))
            self.LayoutImages.addWidget(Image)
            text = QtWidgets.QLabel(self.Images[i][0])
            text.setVisible(False)
            self.LayoutImages.addWidget(text)
        self.ImageShow.addLayout(self.LayoutImages)
        self.StyleCounter=1

    def ShowStyle(self):
        for i in range(self.ImageCounter, len(self.Images)):
            for j in range(self.StyleCounter,len(self.Images[i])):
                Image = QtWidgets.QLabel(self)
                pix = QtGui.QPixmap(self.Images[i][j])
                self.StyleSize = pix.size()
                if self.ImageSize != self.StyleSize:
                    QtWidgets.QMessageBox.warning(self,"Ошибка","Изображение и стили должны быть одного размера")
                    self.Images[i].remove(self.Images[i][j])
                    return
                Image.setPixmap(pix.scaled(140,140))
                self.LayoutImages.addWidget(Image)
        self.StyleCounter+=1

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
        self.ImageCounter-=1