# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 816)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 30, 771, 281))
        self.treeView.setObjectName("treeView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
        self.label.setObjectName("label")
        self.labelVideo1 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo1.setGeometry(QtCore.QRect(820, 40, 171, 16))
        self.labelVideo1.setObjectName("labelVideo1")
        self.labelAudio1 = QtWidgets.QLabel(self.centralwidget)
        self.labelAudio1.setGeometry(QtCore.QRect(820, 70, 171, 16))
        self.labelAudio1.setObjectName("labelAudio1")
        self.labelVideo2 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo2.setGeometry(QtCore.QRect(820, 100, 171, 16))
        self.labelVideo2.setObjectName("labelVideo2")
        self.labelAudio2 = QtWidgets.QLabel(self.centralwidget)
        self.labelAudio2.setGeometry(QtCore.QRect(820, 130, 171, 16))
        self.labelAudio2.setObjectName("labelAudio2")
        self.labelVideo3 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo3.setGeometry(QtCore.QRect(820, 160, 171, 16))
        self.labelVideo3.setObjectName("labelVideo3")
        self.sliderCutoff = QtWidgets.QSlider(self.centralwidget)
        self.sliderCutoff.setGeometry(QtCore.QRect(260, 340, 160, 22))
        self.sliderCutoff.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCutoff.setObjectName("sliderCutoff")
        self.sliderResolution = QtWidgets.QSlider(self.centralwidget)
        self.sliderResolution.setGeometry(QtCore.QRect(260, 380, 160, 22))
        self.sliderResolution.setOrientation(QtCore.Qt.Horizontal)
        self.sliderResolution.setObjectName("sliderResolution")
        self.sliderReduction = QtWidgets.QSlider(self.centralwidget)
        self.sliderReduction.setGeometry(QtCore.QRect(260, 420, 160, 22))
        self.sliderReduction.setOrientation(QtCore.Qt.Horizontal)
        self.sliderReduction.setObjectName("sliderReduction")
        self.labelCutoff = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoff.setGeometry(QtCore.QRect(70, 340, 47, 13))
        self.labelCutoff.setObjectName("labelCutoff")
        self.labelResolution = QtWidgets.QLabel(self.centralwidget)
        self.labelResolution.setGeometry(QtCore.QRect(70, 380, 51, 16))
        self.labelResolution.setObjectName("labelResolution")
        self.labelReduction = QtWidgets.QLabel(self.centralwidget)
        self.labelReduction.setGeometry(QtCore.QRect(70, 420, 91, 21))
        self.labelReduction.setObjectName("labelReduction")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(430, 470, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelCutoffUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffUnits.setGeometry(QtCore.QRect(450, 340, 47, 13))
        self.labelCutoffUnits.setObjectName("labelCutoffUnits")
        self.labelResolutionUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelResolutionUnits.setGeometry(QtCore.QRect(450, 380, 47, 13))
        self.labelResolutionUnits.setObjectName("labelResolutionUnits")
        self.labelReductionUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelReductionUnits.setGeometry(QtCore.QRect(450, 420, 47, 13))
        self.labelReductionUnits.setObjectName("labelReductionUnits")
        self.buttonPlay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlay.setGeometry(QtCore.QRect(210, 540, 75, 23))
        self.buttonPlay.setObjectName("buttonPlay")
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setGeometry(QtCore.QRect(350, 540, 75, 23))
        self.buttonSave.setObjectName("buttonSave")
        self.labelCutoffValue = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffValue.setGeometry(QtCore.QRect(210, 340, 16, 16))
        self.labelCutoffValue.setObjectName("labelCutoffValue")
        self.labelResValue = QtWidgets.QLabel(self.centralwidget)
        self.labelResValue.setGeometry(QtCore.QRect(210, 380, 16, 16))
        self.labelResValue.setObjectName("labelResValue")
        self.labelRedValue = QtWidgets.QLabel(self.centralwidget)
        self.labelRedValue.setGeometry(QtCore.QRect(210, 420, 16, 16))
        self.labelRedValue.setObjectName("labelRedValue")
        self.buttonConvert = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConvert.setGeometry(QtCore.QRect(210, 470, 75, 23))
        self.buttonConvert.setObjectName("buttonConvert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Directory"))
        self.labelVideo1.setText(_translate("MainWindow", "Video 1"))
        self.labelAudio1.setText(_translate("MainWindow", "Audio 1"))
        self.labelVideo2.setText(_translate("MainWindow", "Video 2"))
        self.labelAudio2.setText(_translate("MainWindow", "Audio 2"))
        self.labelVideo3.setText(_translate("MainWindow", "Video 3"))
        self.labelCutoff.setText(_translate("MainWindow", "Cutoff"))
        self.labelResolution.setText(_translate("MainWindow", "Resolution"))
        self.labelReduction.setText(_translate("MainWindow", "Volume Reduction"))
        self.labelCutoffUnits.setText(_translate("MainWindow", "dBFS"))
        self.labelResolutionUnits.setText(_translate("MainWindow", "s / 10"))
        self.labelReductionUnits.setText(_translate("MainWindow", "dBFS"))
        self.buttonPlay.setText(_translate("MainWindow", "Play"))
        self.buttonSave.setText(_translate("MainWindow", "Save"))
        self.labelCutoffValue.setText(_translate("MainWindow", "0"))
        self.labelResValue.setText(_translate("MainWindow", "0"))
        self.labelRedValue.setText(_translate("MainWindow", "0"))
        self.buttonConvert.setText(_translate("MainWindow", "Convert"))

