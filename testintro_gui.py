# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_intro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1358, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.introButton = QtWidgets.QPushButton(self.centralwidget)
        self.introButton.setGeometry(QtCore.QRect(0, 0, 1361, 711))
        self.introButton.setText("")
        self.introButton.setObjectName("introButton")
        self.inicioButton = QtWidgets.QPushButton(self.centralwidget)
        self.inicioButton.setGeometry(QtCore.QRect(1100, 710, 110, 32))
        self.inicioButton.setObjectName("inicioButton")
        self.creditosButton = QtWidgets.QPushButton(self.centralwidget)
        self.creditosButton.setGeometry(QtCore.QRect(1230, 710, 110, 32))
        self.creditosButton.setObjectName("creditosButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1358, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sostenibilidad Urbana"))
        self.inicioButton.setText(_translate("MainWindow", "Inicio"))
        self.creditosButton.setText(_translate("MainWindow", "Creditos"))

