# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 816)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 30, 771, 281))
        self.treeView.setObjectName("treeView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelVideo1 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo1.setGeometry(QtCore.QRect(820, 40, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVideo1.setFont(font)
        self.labelVideo1.setObjectName("labelVideo1")
        self.labelAudio1 = QtWidgets.QLabel(self.centralwidget)
        self.labelAudio1.setGeometry(QtCore.QRect(820, 80, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAudio1.setFont(font)
        self.labelAudio1.setObjectName("labelAudio1")
        self.labelVideo2 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo2.setGeometry(QtCore.QRect(820, 120, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVideo2.setFont(font)
        self.labelVideo2.setObjectName("labelVideo2")
        self.labelAudio2 = QtWidgets.QLabel(self.centralwidget)
        self.labelAudio2.setGeometry(QtCore.QRect(820, 160, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelAudio2.setFont(font)
        self.labelAudio2.setObjectName("labelAudio2")
        self.labelVideo3 = QtWidgets.QLabel(self.centralwidget)
        self.labelVideo3.setGeometry(QtCore.QRect(820, 200, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVideo3.setFont(font)
        self.labelVideo3.setObjectName("labelVideo3")
        self.sliderCutoff = QtWidgets.QSlider(self.centralwidget)
        self.sliderCutoff.setGeometry(QtCore.QRect(200, 380, 160, 22))
        self.sliderCutoff.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCutoff.setObjectName("sliderCutoff")
        self.sliderResolution = QtWidgets.QSlider(self.centralwidget)
        self.sliderResolution.setGeometry(QtCore.QRect(200, 440, 160, 22))
        self.sliderResolution.setOrientation(QtCore.Qt.Horizontal)
        self.sliderResolution.setObjectName("sliderResolution")
        self.sliderReduction = QtWidgets.QSlider(self.centralwidget)
        self.sliderReduction.setGeometry(QtCore.QRect(200, 510, 160, 22))
        self.sliderReduction.setOrientation(QtCore.Qt.Horizontal)
        self.sliderReduction.setObjectName("sliderReduction")
        self.labelCutoff = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoff.setGeometry(QtCore.QRect(150, 350, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCutoff.setFont(font)
        self.labelCutoff.setObjectName("labelCutoff")
        self.labelResolution = QtWidgets.QLabel(self.centralwidget)
        self.labelResolution.setGeometry(QtCore.QRect(150, 410, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelResolution.setFont(font)
        self.labelResolution.setObjectName("labelResolution")
        self.labelReduction = QtWidgets.QLabel(self.centralwidget)
        self.labelReduction.setGeometry(QtCore.QRect(150, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelReduction.setFont(font)
        self.labelReduction.setObjectName("labelReduction")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(360, 640, 331, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.labelCutoffUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffUnits.setGeometry(QtCore.QRect(390, 380, 47, 13))
        self.labelCutoffUnits.setObjectName("labelCutoffUnits")
        self.labelResolutionUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelResolutionUnits.setGeometry(QtCore.QRect(390, 440, 47, 13))
        self.labelResolutionUnits.setObjectName("labelResolutionUnits")
        self.labelReductionUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelReductionUnits.setGeometry(QtCore.QRect(390, 510, 47, 13))
        self.labelReductionUnits.setObjectName("labelReductionUnits")
        self.buttonPlay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlay.setGeometry(QtCore.QRect(490, 700, 75, 23))
        self.buttonPlay.setObjectName("buttonPlay")
        self.labelCutoffValue = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffValue.setGeometry(QtCore.QRect(150, 380, 31, 16))
        self.labelCutoffValue.setObjectName("labelCutoffValue")
        self.labelResValue = QtWidgets.QLabel(self.centralwidget)
        self.labelResValue.setGeometry(QtCore.QRect(150, 440, 31, 16))
        self.labelResValue.setObjectName("labelResValue")
        self.labelRedValue = QtWidgets.QLabel(self.centralwidget)
        self.labelRedValue.setGeometry(QtCore.QRect(150, 510, 31, 16))
        self.labelRedValue.setObjectName("labelRedValue")
        self.buttonConvert = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConvert.setGeometry(QtCore.QRect(490, 580, 75, 23))
        self.buttonConvert.setObjectName("buttonConvert")
        self.sliderChangeTime = QtWidgets.QSlider(self.centralwidget)
        self.sliderChangeTime.setGeometry(QtCore.QRect(660, 440, 160, 22))
        self.sliderChangeTime.setOrientation(QtCore.Qt.Horizontal)
        self.sliderChangeTime.setObjectName("sliderChangeTime")
        self.labelCutoffVideo3 = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffVideo3.setGeometry(QtCore.QRect(610, 350, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCutoffVideo3.setFont(font)
        self.labelCutoffVideo3.setObjectName("labelCutoffVideo3")
        self.labelCutoffVideo3Value = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffVideo3Value.setGeometry(QtCore.QRect(610, 380, 41, 16))
        self.labelCutoffVideo3Value.setObjectName("labelCutoffVideo3Value")
        self.labelCutoffVideo3Units = QtWidgets.QLabel(self.centralwidget)
        self.labelCutoffVideo3Units.setGeometry(QtCore.QRect(850, 380, 47, 13))
        self.labelCutoffVideo3Units.setObjectName("labelCutoffVideo3Units")
        self.labelChangeTimeValue = QtWidgets.QLabel(self.centralwidget)
        self.labelChangeTimeValue.setGeometry(QtCore.QRect(610, 440, 41, 16))
        self.labelChangeTimeValue.setObjectName("labelChangeTimeValue")
        self.labelChangeTime = QtWidgets.QLabel(self.centralwidget)
        self.labelChangeTime.setGeometry(QtCore.QRect(610, 410, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelChangeTime.setFont(font)
        self.labelChangeTime.setObjectName("labelChangeTime")
        self.labelChangeTimeUnits = QtWidgets.QLabel(self.centralwidget)
        self.labelChangeTimeUnits.setGeometry(QtCore.QRect(850, 440, 47, 13))
        self.labelChangeTimeUnits.setObjectName("labelChangeTimeUnits")
        self.sliderCutoffVideo3 = QtWidgets.QSlider(self.centralwidget)
        self.sliderCutoffVideo3.setGeometry(QtCore.QRect(660, 380, 160, 22))
        self.sliderCutoffVideo3.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCutoffVideo3.setObjectName("sliderCutoffVideo3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 21))
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSynchronize_Audio = QtWidgets.QAction(MainWindow)
        self.actionSynchronize_Audio.setObjectName("actionSynchronize_Audio")
        self.actionNormalize_Audio = QtWidgets.QAction(MainWindow)
        self.actionNormalize_Audio.setObjectName("actionNormalize_Audio")
        self.menuSave.addAction(self.actionSave)
        self.menuSave.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSynchronize_Audio)
        self.menuEdit.addAction(self.actionNormalize_Audio)
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

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
        self.labelCutoff.setText(_translate("MainWindow", "Silence Cutoff"))
        self.labelResolution.setText(_translate("MainWindow", "Resolution"))
        self.labelReduction.setText(_translate("MainWindow", "Volume Reduction"))
        self.labelCutoffUnits.setText(_translate("MainWindow", "dBFS"))
        self.labelResolutionUnits.setText(_translate("MainWindow", "s"))
        self.labelReductionUnits.setText(_translate("MainWindow", "dBFS"))
        self.buttonPlay.setText(_translate("MainWindow", "Preview"))
        self.labelCutoffValue.setText(_translate("MainWindow", "0"))
        self.labelResValue.setText(_translate("MainWindow", "0"))
        self.labelRedValue.setText(_translate("MainWindow", "0"))
        self.buttonConvert.setText(_translate("MainWindow", "Convert"))
        self.labelCutoffVideo3.setText(_translate("MainWindow", "Video 3 cutoff"))
        self.labelCutoffVideo3Value.setText(_translate("MainWindow", "0"))
        self.labelCutoffVideo3Units.setText(_translate("MainWindow", "|dBFS|"))
        self.labelChangeTimeValue.setText(_translate("MainWindow", "0"))
        self.labelChangeTime.setText(_translate("MainWindow", "Change Time"))
        self.labelChangeTimeUnits.setText(_translate("MainWindow", "s"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSynchronize_Audio.setText(_translate("MainWindow", "Synchronize Audio"))
        self.actionNormalize_Audio.setText(_translate("MainWindow", "Normalize Audio"))
