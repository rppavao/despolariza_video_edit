# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normalize_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NormalizeWindow(object):
    def setupUi(self, NormalizeWindow):
        NormalizeWindow.setObjectName("NormalizeWindow")
        NormalizeWindow.resize(530, 182)
        self.centralwidget = QtWidgets.QWidget(NormalizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonNormalize = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNormalize.setGeometry(QtCore.QRect(240, 110, 75, 23))
        self.buttonNormalize.setObjectName("buttonNormalize")
        self.labelNormalizeText = QtWidgets.QLabel(self.centralwidget)
        self.labelNormalizeText.setGeometry(QtCore.QRect(50, 20, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelNormalizeText.setFont(font)
        self.labelNormalizeText.setObjectName("labelNormalizeText")
        self.sliderNormalize = QtWidgets.QSlider(self.centralwidget)
        self.sliderNormalize.setGeometry(QtCore.QRect(190, 60, 160, 22))
        self.sliderNormalize.setOrientation(QtCore.Qt.Horizontal)
        self.sliderNormalize.setObjectName("sliderNormalize")
        self.labelNormlizeUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelNormlizeUnits.setGeometry(QtCore.QRect(380, 60, 47, 13))
        self.labelNormlizeUnits.setObjectName("labelNormlizeUnits")
        self.labelNormalizeValue = QtWidgets.QLabel(self.centralwidget)
        self.labelNormalizeValue.setGeometry(QtCore.QRect(140, 60, 31, 16))
        self.labelNormalizeValue.setObjectName("labelNormalizeValue")
        NormalizeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NormalizeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 21))
        self.menubar.setObjectName("menubar")
        NormalizeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NormalizeWindow)
        self.statusbar.setObjectName("statusbar")
        NormalizeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NormalizeWindow)
        QtCore.QMetaObject.connectSlotsByName(NormalizeWindow)

    def retranslateUi(self, NormalizeWindow):
        _translate = QtCore.QCoreApplication.translate
        NormalizeWindow.setWindowTitle(_translate("NormalizeWindow", "MainWindow"))
        self.buttonNormalize.setText(_translate("NormalizeWindow", "Normalize"))
        self.labelNormalizeText.setText(_translate("NormalizeWindow", "Normalize audito to level:"))
        self.labelNormlizeUnits.setText(_translate("NormalizeWindow", "dBFS"))
        self.labelNormalizeValue.setText(_translate("NormalizeWindow", "0"))
