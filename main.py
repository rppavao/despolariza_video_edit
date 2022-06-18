# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:28:37 2022

@author: Rafael Pavão
"""
from video_edit_classes import *

path = input("File location: ")

video_name1 = input("Name of first video: ")
audio_name1 = input("Name of first audio: ")

video_name2 = input("Name of second video: ")
audio_name2 = input("Name of second audio: ")

print(">>>Uploading files...")

video1 = video(video_name1,path)
video1.upload_audio(audio_name1)
video2 = video(video_name2,path)
video2.upload_audio(audio_name2)

print(">>>Finished uploading!")

cutoff = 0 #input("Specify sound cutoff (in db) for third video: ")
resolution = int( input("Time resolution (seconds): ") )
volume_reduction = int( input("Reduction factor (in db): ") )

edit_instance = edit_tools(video1,video2,path=path,parameters=(cutoff, \
                                                resolution,volume_reduction))
    
print(">>>Video processing started...")

edit_instance.concat_video_by_sound()

print(">>>Video processing ended!")
print(">>>New file name 'final_video.mp4' was created!")