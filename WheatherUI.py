# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WheatherUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from pprint import pprint
import tkinter;
from tkinter import messagebox;
from yesno import *
import yesno
class Ui_MainWindow(object):
    def box(self):
        root=tkinter.Tk();
        root.withdraw();
    def wheather(self):
        if(self.txtcityname.text()==""):
            self.hidefunction();
            self.box();
            messagebox.showerror("Input_Error","No City Found");
        else:
            city = self.txtcityname.text();
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=80de22b945895ebb43b6c408eb70cb84&units=metric'.format(city)
            res = requests.get(url)
            data = res.json()
            temp = str(data['main']['temp']);
            wind_speed = str(data['wind']['speed']);
            latitude = str(data['coord']['lat']);
            longitude = str(data['coord']['lon']);
            description = str(data['weather'][0]['description'])
            print('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            self.tempop.setText('{} degree celcius'.format(temp));
            self.windspeedop.setText('{} m/s'.format(wind_speed));
            self.latitudeop.setText('{}'.format(latitude));
            self.longitudeop.setText('{}'.format(longitude));
            self.descriptionop.setText('{}'.format(description));

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 536)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblbg = QtWidgets.QLabel(self.centralwidget)
        self.lblbg.setGeometry(QtCore.QRect(0, 0, 721, 531))
        self.lblbg.setStyleSheet("background-color:white;")
        self.lblbg.setText("")
        self.lblbg.setObjectName("lblbg")
        self.lbltitle = QtWidgets.QLabel(self.centralwidget)
        self.lbltitle.setGeometry(QtCore.QRect(0, 0, 721, 61))
        self.lbltitle.setStyleSheet("color:rgba(241, 90, 34, 1);\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background-color:rgb(46, 49, 49);")
        self.lbltitle.setObjectName("lbltitle")
        self.txtcityname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtcityname.setGeometry(QtCore.QRect(160, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtcityname.setFont(font)
        self.txtcityname.setStyleSheet("")
        self.txtcityname.setObjectName("txtcityname")
        self.btnsearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnsearch.setGeometry(QtCore.QRect(360, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnsearch.setFont(font)
        self.btnsearch.setStyleSheet("background-color:rgba(241, 90, 34, 1);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("searchicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsearch.setIcon(icon)
        self.btnsearch.setObjectName("btnsearch")
        ###############################btn search#########################
        self.btnsearch.clicked.connect(self.wheather);
        self.lbltemp = QtWidgets.QLabel(self.centralwidget)
        self.lbltemp.setGeometry(QtCore.QRect(150, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbltemp.setFont(font)
        self.lbltemp.setObjectName("lbltemp")
        self.tempop = QtWidgets.QLabel(self.centralwidget)
        self.tempop.setGeometry(QtCore.QRect(280, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tempop.setFont(font)
        self.tempop.setObjectName("tempop")
        self.lblwindspeed = QtWidgets.QLabel(self.centralwidget)
        self.lblwindspeed.setGeometry(QtCore.QRect(150, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblwindspeed.setFont(font)
        self.lblwindspeed.setObjectName("lblwindspeed")
        self.windspeedop = QtWidgets.QLabel(self.centralwidget)
        self.windspeedop.setGeometry(QtCore.QRect(280, 270, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.windspeedop.setFont(font)
        self.windspeedop.setObjectName("windspeedop")
        self.lbllatitude = QtWidgets.QLabel(self.centralwidget)
        self.lbllatitude.setGeometry(QtCore.QRect(150, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbllatitude.setFont(font)
        self.lbllatitude.setObjectName("lbllatitude")
        self.latitudeop = QtWidgets.QLabel(self.centralwidget)
        self.latitudeop.setGeometry(QtCore.QRect(280, 330, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.latitudeop.setFont(font)
        self.latitudeop.setObjectName("latitudeop")
        self.lbllongitude = QtWidgets.QLabel(self.centralwidget)
        self.lbllongitude.setGeometry(QtCore.QRect(150, 390, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbllongitude.setFont(font)
        self.lbllongitude.setObjectName("lbllongitude")
        self.longitudeop = QtWidgets.QLabel(self.centralwidget)
        self.longitudeop.setGeometry(QtCore.QRect(280, 390, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.longitudeop.setFont(font)
        self.longitudeop.setObjectName("longitudeop")
        self.lbldescription = QtWidgets.QLabel(self.centralwidget)
        self.lbldescription.setGeometry(QtCore.QRect(150, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbldescription.setFont(font)
        self.lbldescription.setObjectName("lbldescription")
        self.descriptionop = QtWidgets.QLabel(self.centralwidget)
        self.descriptionop.setGeometry(QtCore.QRect(280, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.descriptionop.setFont(font)
        self.descriptionop.setObjectName("descriptionop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbltitle.setText(_translate("MainWindow", "      Current weather in your city"))
        self.txtcityname.setPlaceholderText(_translate("MainWindow", "City Name"))
        self.btnsearch.setText(_translate("MainWindow", "Search"))
        self.lbltemp.setText(_translate("MainWindow", "Temperature"))
        self.tempop.setText(_translate("MainWindow", "-"))
        self.lblwindspeed.setText(_translate("MainWindow", "Wind-Speed"))
        self.windspeedop.setText(_translate("MainWindow", "-"))
        self.lbllatitude.setText(_translate("MainWindow", "Latitude"))
        self.latitudeop.setText(_translate("MainWindow", "-"))
        self.lbllongitude.setText(_translate("MainWindow", "Longitude"))
        self.longitudeop.setText(_translate("MainWindow", "-"))
        self.lbldescription.setText(_translate("MainWindow", "Description"))
        self.descriptionop.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":

    import sys
    self.hidefunction();
    app = QtWidgets.QApplication(sys.argv)
    WheatherUI = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow()
    ui1.setupUi(WheatherUI)
    WheatherUI.show()
    sys.exit(app.exec_())

