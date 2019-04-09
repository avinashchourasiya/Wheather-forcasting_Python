# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random;
import pymysql;
import tkinter;
from tkinter import messagebox;
import Login
from Login import *;
import smtplib;
class Ui_MainWindow(object):
    connection=pymysql.connect("localhost","root","","wheather_prediction");
    cursor=connection.cursor();
    def cancel(self):
        #pass
        Signup.hide();
        sys.exit(app.exec_())
    def box(self):
        root=tkinter.Tk();
        root.withdraw();
    def signin(self):
        try:
            r_num=str(random.randint(12416,99899));
            print(r_num);
            a=self.txtusername.text();
            b=r_num;
            c=self.txtemail.text();
            d=self.txtcontact.text();
            if(a!="" and b !="" and c !=""):
            #sql=("INSERT INTO signup VALUES ('"+a+"','"+b+"','"+c+"','"+c"')");
                sql=("insert into signup values('"+a+"','"+b+"','"+c+"','"+d+"')");
                self.cursor.execute(sql);
                self.connection.commit();
                if(sql):
                    self.box();
                    gmail_user = 'avinashchourasiya88@gmail.com'  
                    gmail_password = 'imoracleyesameen9833avi7678'

                    try:  
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_password)
                        z=server.sendmail('avinashchourasiya88@gmail.com', c,b,"Password")
                        server.close()
                        messagebox.showinfo("SignUp_Info","Signup_successfully \n Please check your Email for password");
                        self.open(); 
                    except:  
                       #print('Something went wrong...');
                        messagebox.showerror("SignUp_Info","Invalid Email");
                        #if(self.z):
                             
                    
            else:
                self.box();
                messagebox.showerror("SignUp_Error","Invalid Details");    

        except Exception as e:
            print(e);

    def open(self):
        self.Login = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.Login)
        self.Login.show()
        Signup.hide();
        #sys.exit(app.exec_())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 417)
        MainWindow.setStyleSheet("Background-color:#34495e;")
        self.signup = QtWidgets.QWidget(MainWindow)
        self.signup.setObjectName("signup")
        self.lbltitle = QtWidgets.QLabel(self.signup)
        self.lbltitle.setGeometry(QtCore.QRect(0, 0, 721, 131))
        self.lbltitle.setStyleSheet("background-color:#336e7b;")
        self.lbltitle.setText("")
        self.lbltitle.setObjectName("lbltitle")
        self.label = QtWidgets.QLabel(self.signup)
        self.label.setGeometry(QtCore.QRect(-10, 30, 391, 51))
        self.label.setStyleSheet("color:white;\n"
"font-size:40px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.signup)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 381, 361))
        self.label_2.setStyleSheet("Background-color:#34495e;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lblusername = QtWidgets.QLabel(self.signup)
        self.lblusername.setGeometry(QtCore.QRect(30, 150, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblusername.setFont(font)
        self.lblusername.setObjectName("lblusername")
        self.lblemail = QtWidgets.QLabel(self.signup)
        self.lblemail.setGeometry(QtCore.QRect(40, 220, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblemail.setFont(font)
        self.lblemail.setObjectName("lblemail")
        self.lblcontact = QtWidgets.QLabel(self.signup)
        self.lblcontact.setGeometry(QtCore.QRect(30, 280, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblcontact.setFont(font)
        self.lblcontact.setObjectName("lblcontact")
        self.txtusername = QtWidgets.QLineEdit(self.signup)
        self.txtusername.setGeometry(QtCore.QRect(160, 150, 171, 31))
        self.txtusername.setMaxLength(10)
        self.txtusername.setClearButtonEnabled(True)
        self.txtusername.setObjectName("txtusername")
        self.txtemail = QtWidgets.QLineEdit(self.signup)
        self.txtemail.setGeometry(QtCore.QRect(160, 210, 171, 31))
        self.txtemail.setClearButtonEnabled(True)
        self.txtemail.setObjectName("txtemail")
        self.txtcontact = QtWidgets.QLineEdit(self.signup)
        self.txtcontact.setGeometry(QtCore.QRect(160, 270, 171, 31))
        self.txtcontact.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtcontact.setMaxLength(10)
        self.txtcontact.setClearButtonEnabled(True)
        self.txtcontact.setObjectName("txtcontact")
        self.btnsignup = QtWidgets.QPushButton(self.signup)
        self.btnsignup.setGeometry(QtCore.QRect(60, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnsignup.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("signup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsignup.setIcon(icon)
        self.btnsignup.setIconSize(QtCore.QSize(20, 20))
        self.btnsignup.setObjectName("btnsignup")
        ############################signup function######################
        self.btnsignup.clicked.connect(self.signin);
        ###################################################################
        self.btncancel = QtWidgets.QPushButton(self.signup)
        self.btncancel.setGeometry(QtCore.QRect(190, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btncancel.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncancel.setIcon(icon1)
        self.btncancel.setIconSize(QtCore.QSize(20, 20))
        self.btncancel.setObjectName("btncancel")
        ############################signup function######################
        self.btncancel.clicked.connect(self.cancel);
        
        ###################################################################
        MainWindow.setCentralWidget(self.signup)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Wheather Forcasting"))
        self.lblusername.setText(_translate("MainWindow", "Username"))
        self.lblemail.setText(_translate("MainWindow", "Email"))
        self.lblcontact.setText(_translate("MainWindow", "Contact"))
        self.btnsignup.setText(_translate("MainWindow", "SignUp"))
        self.btncancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())

