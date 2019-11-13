import sys
from PyQt5 import QtWidgets, QtCore, uic, QtGui
import math


class MainWindow ( QtWidgets.QMainWindow ):
    def __init__(self, parent=None):
        super ( MainWindow, self ).__init__ ( parent)
        self.ui = uic.loadUi ( 'main.ui' )

        self.ui_circle = uic.loadUi('circle.ui')
        self.ui_par = uic.loadUi('paralelogram.ui')
        self.ui_sq = uic.loadUi('square.ui')
        self.ui_tr_r = uic.loadUi('triangle_reg.ui')
        self.ui_tr_u = uic.loadUi('triangle_user.ui')
        self.ui_tr_s = uic.loadUi('triangle_straight.ui')



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
        self.r = int(self.ui_circle.lineEdit.text())
        print(self.r)
        result = self.r*self.r
        self.ui.textEdit.setText(str(result))
        self.ui.textEdit_2.append(str(result))
        self.ui_circle.lineEdit.clear()
        self.ui_circle.close()

    def square(self):
        self.p =  int(self.ui_sq.lineEdit.text())
        print(self.p)
        result = self.p*self.p
        self.ui.textEdit.setText(str(result))
        self.ui.textEdit_2.append(str(result))
        self.ui_sq.close()

    def paralelog(self):
        self.a =  int(self.ui_par.lineEdit.text())
        self.b = int(self.ui_par.lineEdit_2.text())
        result = self.a*self.b
        self.ui.textEdit.setText(str(result))
        self.ui.textEdit_2.append(str(result))
        self.ui_par.close()


    def triangle_riv(self):
         self.p = int(self.ui_tr_r.lineEdit.text())
         result = (math.sqrt(3)/4)*(self.p * self.p)
         self.ui.textEdit.setText(str(result))
         self.ui.textEdit_2.append(str(result))
         self.ui_tr_r.close()

    def triangle_st(self):
         self.a = int(self.ui_tr_s.lineEdit.text())
         self.b = int(self.ui_tr_s.lineEdit_2.text())
         result = 0.5*(self.a * self.b)
         self.ui.textEdit.setText(str(result))
         self.ui.textEdit_2.append(str(result))
         self.ui_tr_s.close()

    def triangle_user(self):
         self.a = int(self.ui_tr_u.lineEdit.text())
         self.b = int(self.ui_tr_u.lineEdit_2.text())
         self.c = int(self.ui_tr_u.lineEdit_3.text())
         p = (self.a+self.b+self.c)/2
         result = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
         self.ui.textEdit.setText(str(result))
         self.ui.textEdit_2.append(str(result))
         self.ui_tr_u.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication ( sys.argv )
    window = MainWindow ()
    sys.exit ( app.exec () )