
from PyQt5 import QtCore, QtGui, QtWidgets
from WheatherUI import *;
import WheatherUI;
from changepassword import *;
import changepassword;
class Ui_yesno(object):
    def yes(self):
        self.changepassword = QtWidgets.QMainWindow()
        self.ui = Ui_changepassword()
        self.ui.setupUi(self.changepassword)
        self.changepassword.show()
        
    def no(self):
        self.WheatherUI = QtWidgets.QMainWindow()
        self.ui1 = Ui_MainWindow()
        self.ui1.setupUi(self.WheatherUI)
        self.WheatherUI.show()
    def setupUi(self, yesno):
        yesno.setObjectName("yesno")
        yesno.resize(302, 157)
        self.yesno2 = QtWidgets.QWidget(yesno)
        self.yesno2.setObjectName("yesno2")
        self.label = QtWidgets.QLabel(self.yesno2)
        self.label.setGeometry(QtCore.QRect(0, 0, 381, 161))
        self.label.setStyleSheet("background-color:grey;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.yesno2)
        self.label_2.setGeometry(QtCore.QRect(44, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.btnyes = QtWidgets.QPushButton(self.yesno2)
        self.btnyes.setGeometry(QtCore.QRect(40, 90, 81, 31))
        ##########################btn yes########################
        self.btnyes.clicked.connect(self.yes);
        ##################################################
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnyes.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnyes.setIcon(icon)
        self.btnyes.setObjectName("btnyes")
        self.btnno = QtWidgets.QPushButton(self.yesno2)
        self.btnno.setGeometry(QtCore.QRect(160, 90, 81, 31))
        ##########################btn yes########################
        self.btnno.clicked.connect(self.no);
        ##################################################
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnno.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnno.setIcon(icon1)
        self.btnno.setObjectName("btnno")
        yesno.setCentralWidget(self.yesno2)

        self.retranslateUi(yesno)
        QtCore.QMetaObject.connectSlotsByName(yesno)

    def retranslateUi(self, yesno):
        _translate = QtCore.QCoreApplication.translate
        yesno.setWindowTitle(_translate("yesno", "MainWindow"))
        self.label_2.setText(_translate("yesno", "Do you want to change your password?"))
        self.btnyes.setText(_translate("yesno", "YES"))
        self.btnno.setText(_translate("yesno", "NO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    yesno = QtWidgets.QMainWindow()
    ui = Ui_yesno()
    ui.setupUi(yesno)
    yesno.show()
    sys.exit(app.exec_())

