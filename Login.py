
from PyQt5 import QtCore, QtGui, QtWidgets
import signup
from signup import *;
import tkinter;
from tkinter import messagebox;
import pymysql;
import changepassword;
from changepassword import *;
class Ui_Login(object):
    connection=pymysql.connect("localhost","root","","wheather_prediction");
    cursor=connection.cursor();
    def funchangepassword(self):
        self.changepassword = QtWidgets.QMainWindow()
        self.ui = Ui_changepassword()
        self.ui.setupUi(self.changepassword)
        self.changepassword.show()
        #Login.hide();
                
    def box(self):
        root=tkinter.Tk();
        root.withdraw();
    def loginfun(self):
        a=self.txtusername.text();
        b=self.txtpassword.text();  
        if(a=="" or b==""):
            #self.hello();
            self.box();
            messagebox.showerror("Login_Error","Invalid username password");
        else:
            sql="select count(*) from  signup where username='"+a+"' and passwd='"+b+"'"
            self.cursor.execute(sql);
            data=self.cursor.fetchone();
            data1=int(data[0]);
            if(data1>=1):
                self.yesno = QtWidgets.QMainWindow()
                self.ui = Ui_yesno()
                self.ui.setupUi(self.yesno)
                self.yesno.show()
                Login.hide()
                #sys.exit(app.exec_())
            else:
                self.box();
                messagebox.showerror("Login_Error","Invalid username password");
                
    def signup_open(self):
        self.Signup = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Signup)
        self.Signup.show()
        Login.hide();
        #sys.exit(app.exec_())

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(721, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.login = QtWidgets.QWidget(Login)
        self.login.setObjectName("login")
        self.lblimg = QtWidgets.QLabel(self.login)
        self.lblimg.setGeometry(QtCore.QRect(0, 160, 751, 431))
        self.lblimg.setText("")
        self.lblimg.setPixmap(QtGui.QPixmap("bc.jpg"))
        self.lblimg.setObjectName("lblimg")
        self.lbltitle = QtWidgets.QLabel(self.login)
        self.lbltitle.setGeometry(QtCore.QRect(0, 0, 721, 181))
        self.lbltitle.setStyleSheet("background-color:#336e7b;")
        self.lbltitle.setText("")
        self.lbltitle.setWordWrap(False)
        self.lbltitle.setObjectName("lbltitle")
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(0, 20, 181, 51))
        self.label.setStyleSheet("color:white;\n"
"font-size:40px;")
        self.label.setObjectName("label")
        self.txtusername = QtWidgets.QLineEdit(self.login)
        self.txtusername.setGeometry(QtCore.QRect(520, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtusername.setFont(font)
        self.txtusername.setStyleSheet("")
        self.txtusername.setMaxLength(10)
        self.txtusername.setClearButtonEnabled(True)
        self.txtusername.setObjectName("txtusername")
        self.txtpassword = QtWidgets.QLineEdit(self.login)
        self.txtpassword.setGeometry(QtCore.QRect(520, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtpassword.setFont(font)
        self.txtpassword.setStyleSheet("")
        self.txtpassword.setMaxLength(10)
        self.txtpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtpassword.setCursorPosition(0)
        self.txtpassword.setClearButtonEnabled(True)
        self.txtpassword.setObjectName("txtpassword")
        self.btnlogin = QtWidgets.QPushButton(self.login)
        self.btnlogin.setGeometry(QtCore.QRect(524, 120, 81, 31))
        ####################################################btn login
        self.btnlogin.clicked.connect(self.loginfun)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnlogin.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnlogin.setIcon(icon1)
        self.btnlogin.setObjectName("btnlogin")

        self.btnsignup = QtWidgets.QPushButton(self.login)
        self.btnsignup.setGeometry(QtCore.QRect(620, 120, 81, 31))
        ##############################btn signup#######################
        self.btnsignup.clicked.connect(self.signup_open);
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnsignup.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("signup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsignup.setIcon(icon2)
        self.btnsignup.setIconSize(QtCore.QSize(20, 20))
        self.btnsignup.setObjectName("btnsignup")
        #############################button Signup######################
        self.btnsignup.clicked.connect(self.signup_open);
        self.label_2 = QtWidgets.QLabel(self.login)
        self.label_2.setGeometry(QtCore.QRect(-10, 70, 201, 51))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:40px;")
        self.label_2.setObjectName("label_2")
        Login.setCentralWidget(self.login)
        self.btnchange = QtWidgets.QPushButton(self.login)
        self.btnchange.setGeometry(QtCore.QRect(520, 150, 181, 23))
        self.btnchange.setStyleSheet("color:rgb(0, 0, 255);")
        self.btnchange.setFlat(True)
        self.btnchange.setObjectName("btnchange")
        #########################btn change#################
        self.btnchange.clicked.connect(self.funchangepassword);
        Login.setCentralWidget(self.login)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label.setText(_translate("Login", "Wheather"))
        self.txtusername.setPlaceholderText(_translate("Login", "USERNAME"))
        self.txtpassword.setPlaceholderText(_translate("Login", "PASSWORD"))
        self.btnlogin.setText(_translate("Login", "Login"))
        self.btnsignup.setText(_translate("Login", "SignUp"))
        self.label_2.setText(_translate("Login", " Forcasting"))
        self.btnchange.setText(_translate("Login", "change password ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

