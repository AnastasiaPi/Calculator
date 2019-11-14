import sys
from PyQt5 import QtWidgets, QtCore, uic, QtGui
from PyQt5.QtWidgets import *
import math


class MainWindow ( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( MainWindow, self ).__init__ ( parent)
        self.ui = uic.loadUi ( 'source_ui/main.ui' )

        self.ui_circle = uic.loadUi('source_ui/circle.ui')
        self.ui_par = uic.loadUi('source_ui/paralelogram.ui')
        self.ui_sq = uic.loadUi('source_ui/square.ui')
        self.ui_tr_r = uic.loadUi('source_ui/triangle_reg.ui')
        self.ui_tr_u = uic.loadUi('source_ui/triangle_user.ui')
        self.ui_tr_s = uic.loadUi('source_ui/triangle_straight.ui')

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Warning")
        self.msg.setText("Data is not correct", )

        self.cb = self.ui.comboBox

        self.ui.pushButton.clicked.connect(self.check)

        self.ui.show()
    def check(self):
        text = self.cb.currentText()

        if text == "Коло":
            self.ui_circle.show()
            self.ui_circle.pushButton.clicked.connect(self.circle)

        if text=="Квадрат":
            self.ui_sq.show()
            self.ui_sq.pushButton.clicked.connect(self.square)


        if text=="Прямокутник":
            self.ui_par.show()
            self.ui_par.pushButton.clicked.connect(self.paralelog)

        if text=="Трикутник рівнобедрений":
            self.ui_tr_r.show()
            self.ui_tr_r.pushButton.clicked.connect(self.triangle_riv)

        if text=="Трикутник прямокутний":
            self.ui_tr_s.show()
            self.ui_tr_s.pushButton.clicked.connect(self.triangle_st)

        if text=="Трикутник довільний":
            self.ui_tr_u.show()
            self.ui_tr_u.pushButton.clicked.connect(self.triangle_user)

    def circle(self):
        try:
            self.r = int(self.ui_circle.lineEdit.text())
            result = self.r*self.r
            self.ui.textEdit.setText(str(result))
            self.ui.textEdit_2.append(str(result))
            self.ui_circle.lineEdit.clear()
            self.ui_circle.close()
        except ValueError:
            self.msg.show()

    def square(self):
        try:
            self.p =  int(self.ui_sq.lineEdit.text())
            result = self.p*self.p
            self.ui.textEdit.setText(str(result))
            self.ui.textEdit_2.append(str(result))
            self.ui_sq.lineEdit.clear()
            self.ui_sq.close()
        except ValueError:
            self.msg.show()

    def paralelog(self):
        try:
            self.a =  int(self.ui_par.lineEdit.text())
            self.b = int(self.ui_par.lineEdit_2.text())
            result = self.a*self.b
            self.ui.textEdit.setText(str(result))
            self.ui.textEdit_2.append(str(result))
            self.ui_par.lineEdit.clear()
            self.ui_par.lineEdit_2.clear()
            self.ui_par.close()
        except ValueError:
            self.msg.show()


    def triangle_riv(self):
        try:
             self.p = int(self.ui_tr_r.lineEdit.text())
             result = (math.sqrt(3)/4)*(self.p * self.p)
             self.ui.textEdit.setText(str(result))
             self.ui.textEdit_2.append(str(result))
             self.ui_tr_r.lineEdit.clear()
             self.ui_tr_r.close()
        except ValueError:
            self.msg.show()

    def triangle_st(self):
        try:
             self.a = int(self.ui_tr_s.lineEdit.text())
             self.b = int(self.ui_tr_s.lineEdit_2.text())
             result = 0.5*(self.a * self.b)
             self.ui.textEdit.setText(str(result))
             self.ui.textEdit_2.append(str(result))
             self.ui_tr_s.lineEdit.clear()
             self.ui_tr_s.lineEdit_2.clear()
             self.ui_tr_s.close()
        except ValueError:
            self.msg.show()

    def triangle_user(self):
        try:
             self.a = int(self.ui_tr_u.lineEdit.text())
             self.b = int(self.ui_tr_u.lineEdit_2.text())
             self.c = int(self.ui_tr_u.lineEdit_3.text())
             p = (self.a+self.b+self.c)/2
             result = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
             self.ui.textEdit.setText(str(result))
             self.ui.textEdit_2.append(str(result))
             self.ui_tr_u.lineEdit.clear()
             self.ui_tr_u.lineEdit_2.clear()
             self.ui_tr_u.lineEdit_3.clear()
             self.ui_tr_u.close()
        except ValueError:
            self.msg.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWindow ()
    sys.exit ( app.exec () )