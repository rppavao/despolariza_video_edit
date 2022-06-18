# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 23:28:37 2022

@author: Rafael Pavão
"""
from video_edit_classes import *

path = input("File location: ")

video_name1 = input("Name of first video (mp4): ")
audio_name1 = input("Name of first audio (wav): ")

video_name2 = input("Name of second video (mp4): ")
audio_name2 = input("Name of second audio (wav): ")

video_name3 = input("Name of third video (optional): ")

print(">>>Uploading files...")

video1 = video(video_name1,path)
video1.upload_audio(audio_name1)
video2 = video(video_name2,path)
video2.upload_audio(audio_name2)
if video_name3 != '':
    video3 = video(video_name3,path)

print(">>>Finished uploading!")

cutoff = int( input("Specify sound cutoff (in dBFS [-inf,0]) for third video: ") )
resolution = int( input("Time resolution (seconds): ") )
volume_reduction = 0 #int( input("Reduction factor (in dBFS [-inf,0]): ") )

edit_instance = edit_tools(video1,video2,video3=video3,path=path,parameters=(cutoff, \
                                                resolution,volume_reduction))
    
print(">>>Video processing started...")

edit_instance.concat_video_by_sound()

print(">>>Video processing ended!")
print(">>>New file name 'final_video.mp4' was created!")