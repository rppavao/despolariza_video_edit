# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:48:38 2022

@author: Acer
"""
import moviepy.editor as me
import wave as wv
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

class video:
    def __init__(self,video_name='',path='',*video_file):
        
        self.path = path
        self.video_name = video_name
        if video_name != '':        
            self.video_file = me.VideoFileClip(path + video_name)       
            self.audio_file = self.video_file.audio
            self.audio_file_wav = self.audio_file
        elif video_file != ():
            self.video_file = video_file[0]
         
    def concatenate(self,other,name = "concat_video"):
        
        result_video = video(name,self.path)
        result_video.video_file = me.concatenate_videoclips([self.video_file, \
                                                          other.video_file],method='compose')
        result_video.audio_file = result_video.video_file.audio
        
        return result_video
    
    def save_video(self):
        me.write_videofile(self.path + self.name)
        
    def convert_audio(self):
        return
        
class edit_tools:
    def __init__(self,video1,video2,path=''):
        self.path = path
        self.higher_sound = []
        self.video1 = video1
        self.video2 = video2
    
    def get_highest_sound_map(self):        
        time = 0
        
        self.video1.convert_audio()
        self.video2.convert_audio()   
        
        audio_file1 = self.video1.audio_file_wav
        audio_file2 = self.video2.audio_file_wav
        
        for dummy1 in range(audio_file1.getnframes()): #get smallest audio
        
            audio1_frame = audio_file1.readframes(1)
            audio2_frame = audio_file2.readframes(1)
            
            audio1_value = wv.struct.unpack("<h", audio1_frame)             
            audio2_value = wv.struct.unpack("<h", audio2_frame)
        
            rate = audio_file1.getframerate()
            
            time += 1 / float(rate)
        
            if abs(audio1_value[0]) > abs(audio2_value[0]):
                video_id = 1
            else:
                video_id = 2       
        
            if self.higher_sound[-1][1] == video_id :
                self.higher_sound[-1][1] = time
            else:
                self.higher_sound.append([time,video_id])


    def concat_video_by_sound(self):
        first = True
        previous_time = 0
        
        for i in self.higher_sound:
            
            current_time = i[0]
            
            if i[1] == 1:
                clip_name = self.video1.path + self.video1.video_name
            else:
                clip_name = self.video2.path + self.video2.video_name       
            
            subclip = ffmpeg_extract_subclip(clip_name, previous_time , \
                                             current_time, targetname="subclip.mp4")
            
            if first == True:
                final_video = subclip
                first = False
            else:
                final_video = me.concatenate_videoclips([final_video, subclip])
            
            previous_time = current_time
            
        final_video.write_videofile(self.path + "video_by_sound.mp4")
        
            
    
    