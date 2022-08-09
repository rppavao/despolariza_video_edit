# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:28:37 2022

@author: Rafael Pavão
"""
from video_edit_classes import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from screen import Ui_MainWindow
from normalizescreen import Ui_NormalizeWindow
from PyQt5.QtCore import QUrl

class videoEditGui(qtw.QMainWindow):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.set_directory_tree()
        self.video_list = []
        self.audio_list = []
        self.msg = QMessageBox()
        self.slider_values = [0,0,0,0,0]
        self.set_slider_default_value()
        self.ui.progressBar.hide()
        # self.ui.buttonSave.hide()
        self.ui.buttonPlay.hide()
        self.final_video_name = "final_video.mp4"
        self.final_video_instance = False
        self.max_fps = 0
        
        self.ui.treeView.doubleClicked.connect(self.treeView_doubleClicked)
        self.ui.sliderCutoff.valueChanged[int].connect(lambda x: self.get_slider_value(x,slider=0))
        self.ui.sliderResolution.valueChanged[int].connect(lambda x: self.get_slider_value(x,slider=1))
        self.ui.sliderReduction.valueChanged[int].connect(lambda x: self.get_slider_value(x,slider=2))
        self.ui.sliderCutoffVideo3.valueChanged[int].connect(lambda x: self.get_slider_value(x,slider=3))
        self.ui.sliderChangeTime.valueChanged[int].connect(lambda x: self.get_slider_value(x,slider=4))

        self.ui.buttonConvert.clicked.connect(self.start_video_conversion)  
        self.ui.buttonPlay.clicked.connect(self.play_final_video)
        
        self.ui.actionSave.triggered.connect(self.save_video)
        self.ui.actionNormalize_Audio.triggered.connect(self.normalize_audio)

        
    def set_directory_tree(self):
        model = qtw.QFileSystemModel()
        model.setRootPath(qtc.QDir.currentPath())
        
        treeView = self.ui.treeView
        treeView.setModel(model)

    def treeView_doubleClicked(self,index):
        file_name = index.model().filePath(index)
        
        if file_name[-3:] == 'mp4':
            if len(self.video_list) < 3:
                self.video_list.append(file_name)
            else:
                self.video_list = [file_name]
                
        elif file_name[-3:] == 'wav':
            if len(self.audio_list) < 3:
                self.audio_list.append(file_name)
            else:
                self.audio_list = [file_name]
        else:
            self.trigger_error(3)
                
        videoLabel = {0:self.ui.labelVideo1, 1:self.ui.labelVideo2, 2:self.ui.labelVideo3}
        audioLabel = {0:self.ui.labelAudio1, 1:self.ui.labelAudio2}
        
        for i in range(len(self.audio_list)):
            try:
                label = audioLabel[i]
                name = self.audio_list[i].split('/')[-1]
                label.setText(name)
            except KeyError:
                continue
            
        for i in range(len(self.video_list)):
            try:
                label = videoLabel[i]
                name = self.video_list[i].split('/')[-1]
                label.setText(name)
            except KeyError:
                continue
            
    def get_slider_value(self,value,slider):
        
        sliderLabelList = (self.ui.labelCutoffValue, self.ui.labelResValue, self.ui.labelRedValue, \
                           self.ui.labelCutoffVideo3Value, self.ui.labelChangeTimeValue )
            
        self.slider_values[slider] = value
        
        if slider in (1,4):
            value = value / 10
            value_str = "{0:.2f}".format(value)
        else:
            value_str = str(value)
        
        sliderLabelList[slider].setText(value_str)
        
    def set_slider_default_value(self):
        self.ui.labelCutoffValue.setText("-30")
        self.ui.labelResValue.setText("0.5")
        self.ui.labelRedValue.setText("0")
        self.ui.labelCutoffVideo3Value.setText("5")
        self.ui.labelChangeTimeValue.setText("0.5")        
        
        self.ui.sliderCutoff.setMaximum(0)
        self.ui.sliderCutoff.setMinimum(-100)
        self.ui.sliderCutoff.setValue(-50)

        self.ui.sliderResolution.setMaximum(50)
        self.ui.sliderResolution.setMinimum(1)
        self.ui.sliderResolution.setValue(5)
        
        self.ui.sliderReduction.setMaximum(0)
        self.ui.sliderReduction.setMinimum(-100)
        self.ui.sliderReduction.setValue(0)
        
        self.ui.sliderCutoffVideo3.setMaximum(100)
        self.ui.sliderCutoffVideo3.setMinimum(0)
        self.ui.sliderCutoffVideo3.setValue(5)

        self.ui.sliderChangeTime.setMaximum(50)
        self.ui.sliderChangeTime.setMinimum(1)
        self.ui.sliderChangeTime.setValue(5)        
        
    def start_video_conversion(self):
        if len(self.video_list) < 3 or \
            len(self.audio_list) < 2:
            self.trigger_error(0)
            return

        self.ui.progressBar.show()
        
            
        video1 = video(self.video_list[0])
        video1.upload_audio(self.audio_list[0])
        video2 = video(self.video_list[1])
        video2.upload_audio(self.audio_list[1])
        video3 = video(self.video_list[2])
        
        cutoff = self.ui.sliderCutoff.value()
        resolution = self.ui.sliderResolution.value() / 10
        volumeReduction = self.ui.sliderReduction.value()
        cutoffVideo3 = self.ui.sliderCutoffVideo3.value()
        changeTime = self.ui.sliderChangeTime.value() / 10  
        
        # if changeTime > resolution:
        #     print(changeTime,resolution)
        #     self.trigger_error(1)
        #     return
        
        parameters = (cutoff,resolution,volumeReduction,cutoffVideo3,changeTime)
        
        edit_instance = edit_tools(video1,video2,video3=video3,parameters=parameters)
            
        self.final_video_name,self.final_video_instance, \
            self.max_fps = edit_instance.concat_video_by_sound(progress = self.get_progress) 
            
        self.final_video_instance.change_audio(self.final_video_instance.audio_file,True)
        self.final_video_instance.save_video("temp_video.mp4",self.max_fps)
        
        self.get_progress(100)
        
        self.ui.buttonPlay.show()
        
    def get_progress(self, value):
        self.ui.progressBar.setValue(value)
        
    def save_video(self):
        self.final_video_instance.save_video(self.final_video_name,self.max_fps)
        
    def play_final_video(self):
        
        video = QVideoWidget()
        video.resize(300, 300)
        video.move(0, 0)
        
        player = QMediaPlayer()
        player.setVideoOutput(video)
        player.setMedia(QMediaContent(QUrl.fromLocalFile("temp_video.mp4")))
        player.setVideoOutput(video)
        player.play()
        video.show()
        video.exec_()
        print("Here")
        return 
        
    def trigger_error(self,error):
        
        errors = ("Please select 3 videos and 2 audios!", \
                  "Change time must be smaller than Resolution!",\
                  "Video and audio files should be .mp4 and .wav, respectively!",\
                  "Please select 2 audios!")
        
        self.msg.setWindowTitle("Error")
        self.msg.setText(errors[error])
        msg = self.msg.exec_()
        
    def normalize_audio(self):
        if len(self.audio_list) < 2:
            self.trigger_error(3)
            return      
        self.normalizeWindow = normalizeGui(self.audio_list[0],self.audio_list[1] \
                                           ,self.ui.sliderResolution.value() / 10)
        self.normalizeWindow.showWindow()
             
        
class normalizeGui(qtw.QMainWindow):
    
    def __init__(self,audio1,audio2,sliceSize,*args,**kwargs):
        super().__init__(*args,**kwargs)  

        self.window =  qtw.QMainWindow()
        self.ui = Ui_NormalizeWindow()
        self.ui.setupUi(self.window)           
        
        self.targetDBFS = self.getMaxAudioValue(audio1,audio2,sliceSize)
    
        self.setSliderValues()    
    
        self.ui.sliderNormalize.valueChanged[int].connect(self.getSliderValue)

        self.ui.buttonNormalize.clicked.connect(lambda x: self.normalizeAudio(audio1,audio2))

    def showWindow(self):
        self.window.show()
        
    def normalizeAudio(self,audio1,audio2):
        tools = edit_tools()
        tools.normalize_audio(audio1,self.targetDBFS)
        tools.normalize_audio(audio2,self.targetDBFS)
    
    def setSliderValues(self):
        self.ui.labelNormalizeValue.setText(str(self.targetDBFS))      
        
        self.ui.sliderNormalize.setMaximum(0)
        self.ui.sliderNormalize.setMinimum(-100)
        self.ui.sliderNormalize.setValue(int(self.targetDBFS))        
    
    def getSliderValue(self,value):      
        self.targetDBFS = value  
        self.ui.labelNormalizeValue.setText(str(value))
        
        
    def getMaxAudioValue(self,audio1,audio2,sliceSize):
        tools = edit_tools()
        
        max1 = tools.get_max_audio(audio1,sliceSize)
        max2 = tools.get_max_audio(audio2,sliceSize)
        
        return max(max1,max2)
        

if __name__ == "__main__" :
    app = qtw.QApplication([])
    screen = videoEditGui()
    screen.show()
    app.exec_()