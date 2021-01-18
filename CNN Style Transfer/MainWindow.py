from Dialog import Dialog
from Controller import Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

from ProgressBarDialog import ProgressBarDialog
from MainWindowUi import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.Images=[]
        self.GenerateImage=None

        self.Image.setScaledContents(True)

        self.frame.setVisible(False)

        self.TakeImage.triggered.connect(self.TakeImages)
        self.ExitMenu.triggered.connect(self.Exit)
        self.Ref.triggered.connect(self.Reference)
        self.HelpBut.triggered.connect(self.Help)

        self.ImagesTake.clicked.connect(self.TakeImages)
        self.NumStepButton.clicked.connect(self.Loading)
        self.SaveImageButton.clicked.connect(self.Save)
        self.ExitButton.clicked.connect(self.Exit)
        self.CancelButton.clicked.connect(self.Cancel)
        self.ExitMenu.triggered.connect(self.Exit)

        self.Control = Controller()

        QtWidgets.QMessageBox.information(self,"Device",f'Your calculations devise is {self.Control.Network.calculationDevice}')
    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)  
    def Help(self):
        QtWidgets.QMessageBox.information(self,"Помощь","Для правильной работы с программой необходимо выбрать изображение"
                                          +" и стили к нему с одинаковым разрешением (размером).\nДля этого в пункте меню"
                                          +" выберите Выбрать изображение или нажмите на кнопку по середине экрана.\nДалее"
                                          +" выберите изображения и стили к ним, они будут появляться слева от кнопок."
                                          +"\nДалее нажмите кнопку применить.\nДалее необходимо указать степень смешивания,"
                                          +" стиля на изображение и нажмать принять.\n"
                                          +"Степень смешивания указывается от 1 до 9999 (желательно указать число, до 2000, а лучше до 500)"
                                          +"\n Степень смешивания задает количество итераций программы - чем больше, тем стиль сильнее выражается"
                                          +"\nПрограмма обработает ваше изображение и выведет его на экран.")

    def Reference(self):
        QtWidgets.QMessageBox.information(self,"Справка","Данный программный продукт предназначен для реализации"
                                          +" алгоритма Neural Style Transfer.\nСуть алгоритма заключается в том, что"
                                          +" исходное изображение наделяется стилевыми особенностями изображения стиля.\n"
                                          +"Таким образом, вы можете обработать фото или изображение интересным образом"
                                          +" не тратя на это своё собственное время. Программа сделает все сама.\n\n\n\t\t\t\t\t\t\t\t"
                                          +"© Даниил Ментяк")

    def ConfirmMode(self):

        if len(self.Images) == 0:
            self.ImagesTake.setVisible(True)
            return

        self.Image.setPixmap(QtGui.QPixmap(self.Images[0][0]).scaled(512,512))
        self.Control.InitializeNetworkImages(self.Images)

        self.Image.setVisible(True)
        self.frame.setVisible(True)
        self.NumStepButton.setVisible(True)
        self.NumStepsBox.setVisible(True)
        self.NumStepsLabel.setVisible(True)
        self.SaveImageButton.setVisible(False)
        self.ExitButton.setVisible(False)
        self.CancelButton.setVisible(False)

    def TakeImages(self):

        dial = Dialog(self)
        dial.show()
        stop=False
        while not stop:
            for i in  range(self.verticalLayout.count()):
                layoutItem = self.verticalLayout.itemAt(i);
                if (layoutItem.spacerItem()):
                    self.verticalLayout.removeItem(layoutItem);
                    del layoutItem
                    break
                if i+1 == self.verticalLayout.count():
                    stop=True
        self.Image.setVisible(False)
        self.ImagesTake.setVisible(False)

    def Loading(self):

        Bar = ProgressBarDialog(self)

        geo = self.geometry()
        x=geo.x()+((geo.width()/2)-132)
        y=geo.y()+((geo.height()/2)-31)
        Bar.setGeometry(x, y, 265, 62)
        Bar.show()

        self.TakeNumSteps()

        Bar.close()

    def TakeNumSteps(self):

        self.Control.SetNumSteps(self.NumStepsBox.value())

        self.NumStepButton.setVisible(False)
        self.NumStepsBox.setVisible(False)
        self.NumStepsLabel.setVisible(False)
        self.SaveImageButton.setVisible(True)
        self.ExitButton.setVisible(True)
        self.CancelButton.setVisible(True)
        self.frame.setVisible(False)

        QtWidgets.QMessageBox.information(self,"Информация","Запуск алгоритма преобразования")

        self.GenerateImage = self.Control.RunNetwork()
        self.Image.setPixmap(QtGui.QPixmap.fromImage(self.GenerateImage))

        self.frame.setVisible(True)

    def Save(self):

        self.Control.SaveImage(self.GenerateImage)
        self.GenerateImage = None

        self.Image.setVisible(False)
        self.frame.setVisible(False)

        QtWidgets.QMessageBox.information(self,"Информация","Изображение сохранено в папку GeneratedImages")

        self.ConfirmMode()

    def Cancel(self):

        self.GenerateImage = None

        self.Image.setVisible(False)
        self.frame.setVisible(False)

        self.ConfirmMode()

    def Exit(self):

        if QtWidgets.QMessageBox.warning(self,"Предупреждение",
                                         "Приложение закроется без дальнейшего продолжения.\nВас это устраивает?",
                                         QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.No:
            return

        self.close()
        sys.exit()

app=QtWidgets.QApplication(sys.argv)

Window = MainWindow()
Window.show()

sys.exit(app.exec_())
