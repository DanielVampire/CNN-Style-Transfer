from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.uic as uic

from ProgressBarUi import Ui_Dialog

class ProgressBarDialog(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self,parent = None):
        super().__init__(parent,QtCore.Qt.Window)
        self.setupUi(self)

