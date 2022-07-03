# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:28:37 2022

@author: Rafael Pavão
"""
from video_edit_classes import *
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from screen import Ui_MainWindow

class videoEditGui(qtw.QMainWindow):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.set_directory_tree()
        self.video_list = []
        self.audio_list = []
        
        self.ui.treeView.doubleClicked.connect(self.treeView_doubleClicked)
        
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
                self_video_list = [file_name]

        if file_name[-3:] == 'wav':
            if len(self.audio_list) < 3:
                self.audio_list.append(file_name)
            else:
                self_audio_list = [file_name]
                
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
        
# path = input("File location: ")

# video_name1 = input("Name of first video (mp4): ")
# audio_name1 = input("Name of first audio (wav): ")

# video_name2 = input("Name of second video (mp4): ")
# audio_name2 = input("Name of second audio (wav): ")

# video_name3 = input("Name of third video (optional): ")

# print(">>>Uploading files...")

# video1 = video(video_name1,path)
# video1.upload_audio(audio_name1)
# video2 = video(video_name2,path)
# video2.upload_audio(audio_name2)
# if video_name3 != '':
#     video3 = video(video_name3,path)

# print(">>>Finished uploading!")

# cutoff = int( input("Specify sound cutoff (in dBFS [-inf,0]) for third video: ") )
# resolution = int( input("Time resolution (seconds): ") )
# volume_reduction = 0 #int( input("Reduction factor (in dBFS [-inf,0]): ") )

# edit_instance = edit_tools(video1,video2,video3=video3,path=path,parameters=(cutoff, \
#                                                 resolution,volume_reduction))
    
# print(">>>Video processing started...")

# edit_instance.concat_video_by_sound()

# print(">>>Video processing ended!")
# print(">>>New file name 'final_video.mp4' was created!")


if __name__ == "__main__" :
    app = qtw.QApplication([])
    screen = videoEditGui()
    screen.show()
    app.exec_()