from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter;
from tkinter import messagebox;
import pymysql;
class Ui_changepassword(object):
    connection=pymysql.connect("localhost","root","","wheather_prediction");
    cursor=connection.cursor();
    def box(self):
        root=tkinter.Tk();
        root.withdraw();
    def cancel(self):
        changepassword.hide()
    def change(self):
        a=self.txtemail.text();
        b=self.txtoldpassword.text();
        c=self.txtnewpassword.text();
        if(a=="" or b=="" or c==""):
            self.box();
            messagebox.showerror("Login_Error","Invalid username password");
        else:
            sql="UPDATE signup SET passwd='"+c+"' where email='"+a+"' and passwd='"+b+"'"
            self.cursor.execute(sql);
            self.connection.commit();
            data=self.cursor.fetchone();
            self.box();
            messagebox.showerror("Password Change","Password Changed Successfully");
           # print(self.cursor.execute(sql))
           # print(self.connection.commit());
           # if(sql>='1'):
           #     print("changed");
          #  else:
             #   print("notchanged");
            


    def setupUi(self, changepassword):
        changepassword.setObjectName("changepassword")
        changepassword.resize(297, 329)
        self.centralwidget = QtWidgets.QWidget(changepassword)
        self.centralwidget.setObjectName("centralwidget")
        self.lblbg = QtWidgets.QLabel(self.centralwidget)
        self.lblbg.setGeometry(QtCore.QRect(0, 0, 301, 371))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblbg.setFont(font)
        self.lblbg.setStyleSheet("background-color:grey;")
        self.lblbg.setText("")
        self.lblbg.setObjectName("lblbg")
        self.lbltitle = QtWidgets.QLabel(self.centralwidget)
        self.lbltitle.setGeometry(QtCore.QRect(0, 0, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.lbltitle.setFont(font)
        self.lbltitle.setStyleSheet("color:rgba(241, 90, 34, 1);\n"
"font-size:32px;\n"
"font-weight:bold;\n"
"background-color:rgb(46, 49, 49);")
        self.lbltitle.setObjectName("lbltitle")
        self.txtoldpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtoldpassword.setGeometry(QtCore.QRect(40, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtoldpassword.setFont(font)
        self.txtoldpassword.setMaxLength(10)
        self.txtoldpassword.setClearButtonEnabled(True)
        self.txtoldpassword.setObjectName("txtoldpassword")
        self.txtnewpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtnewpassword.setGeometry(QtCore.QRect(40, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtnewpassword.setFont(font)
        self.txtnewpassword.setMaxLength(10)
        self.txtnewpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtnewpassword.setClearButtonEnabled(True)
        self.txtnewpassword.setObjectName("txtnewpassword")
        self.btnno = QtWidgets.QPushButton(self.centralwidget)
        self.btnno.setGeometry(QtCore.QRect(140, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnno.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnno.setIcon(icon)
        self.btnno.setObjectName("btnno")
        self.btnyes = QtWidgets.QPushButton(self.centralwidget)
        self.btnyes.setGeometry(QtCore.QRect(50, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnyes.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnyes.setIcon(icon1)
        self.btnyes.setObjectName("btnyes")
        self.txtemail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtemail.setGeometry(QtCore.QRect(40, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtemail.setFont(font)
        self.txtemail.setMaxLength(50)
        self.txtemail.setClearButtonEnabled(True)
        self.txtemail.setObjectName("txtemail")
        changepassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(changepassword)
        QtCore.QMetaObject.connectSlotsByName(changepassword)

    def retranslateUi(self, changepassword):
        _translate = QtCore.QCoreApplication.translate
        changepassword.setWindowTitle(_translate("changepassword", "MainWindow"))
        self.lbltitle.setText(_translate("changepassword", " Change Password"))
        self.txtoldpassword.setPlaceholderText(_translate("changepassword", "Old Password"))
        self.txtnewpassword.setPlaceholderText(_translate("changepassword", "New Password"))
        self.btnno.setText(_translate("changepassword", "Cancel"))
        self.btnyes.setText(_translate("changepassword", "Change"))
        self.txtemail.setPlaceholderText(_translate("changepassword", "Your Email"))
        ##################btn change######################
        self.btnyes.clicked.connect(self.change);
        ##################btn change######################
        self.btnno.clicked.connect(self.cancel);

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepassword = QtWidgets.QMainWindow()
    ui = Ui_changepassword()
    ui.setupUi(changepassword)
    changepassword.show()
    sys.exit(app.exec_())

