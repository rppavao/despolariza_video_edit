# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:48:38 2022

@author: Rafael Pavão
"""
import moviepy.editor as me
import wave as wv
import pydub as pd
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pydub.utils import make_chunks

class video:
    def __init__(self,video_name='',path='',video_file=False,audio_name=''):
        
        self.path = path
        self.video_name = video_name
        if video_name != '':        
            self.video_file = me.VideoFileClip(path + video_name)       
        elif video_file != False:
            self.video_file = video_file
        
        self.audio_type = 'wav'
        
        if audio_name == '':
            self.audio_file = self.video_file.audio
        else:
            self.upload_audio(audio_name)
            self.audio_type = audio_name.split('.')[-1]
         
    def concatenate(self,other,name = "concat_video",save=True):
        
        result_video = video(name,self.path)
        result_video.video_file = me.concatenate_videoclips([self.video_file, \
                                                          other.video_file],method='compose')
        result_video.audio_file = result_video.video_file.audio
        
        if save == True:
            result_video.save_video()
        
        return result_video
    
    def save_video(self,new_name = '',fps=60):
        if new_name != '':
            self.name =  new_name
        
        self.video_file.write_videofile(self.path + self.name, fps=fps, codec="mpeg4")
        self.save_audio(new_name)
        
        
    def save_audio(self,new_name=''):
        if new_name != '':
           self.name =  new_name
    
        audio_name = self.path + self.name[:len(self.name)-4] + '.' + self.audio_type
        
        self.audio_file.export(audio_name, format= self.audio_type)
    
    def upload_audio(self,audio_file_name):
        if self.audio_type == 'wav':
            input_audio = pd.AudioSegment.from_wav(self.path + audio_file_name)
        self.change_audio(input_audio)         
    
    def change_audio(self,new_audio_file,in_video = False):
        self.audio_file = new_audio_file    
        
        if in_video == True:
            temp_name = self.path+"temp_audio." + self.audio_type
        
            self.save_audio(temp_name)
            new_audioclip = me.AudioFileClip(temp_name)
            self.video_file.audio = new_audioclip
        
    def remove_audio(self):
        self.video_file = self.video_file.without_audio()
    
        
class edit_tools:
    def __init__(self,video1='',video2='',video3=False,path='',parameters=(0,0,0,0,0)):
        self.path = path
        self.higher_sound = []
        self.video1 = video1
        self.video2 = video2
        self.video3 = video3
        if video3 !=False:
            self.video3.remove_audio()
        if parameters[0] == 0:
            self.cutoff = float('-inf')
        else:
            self.cutoff = parameters[0]
        if parameters[3] == 0:
            self.cutoff_video3 = float('-inf')
        else:
            self.cutoff_video3 = parameters[3]
        self.convert_time = 1000 #seconds -> miliseconds
        self.resolution = parameters[1] * self.convert_time
        self.volume_reduction_factor = parameters[2]
        self.change_time = parameters[4] * self.convert_time
    
    def get_highest_sound_map(self,audio_file1,audio_file2,audio_duration,\
                              time_resolution=1000,volume_reduction_factor=0):        
        time = 0

        higher_sound = []
        
        first_iteration = True
        
        if time_resolution == 0:
            time_resolution = 1000
            
        time_difference = time_resolution
    
        while time <= audio_duration and time_difference != 0:
            
            audio_piece1 = audio_file1[time:time + time_difference]
            audio_piece2 = audio_file2[time:time + time_difference] 
    
            audio1_dBFS = audio_piece1.dBFS
            audio2_dBFS = audio_piece2.dBFS
   
            audio_piece1 = audio_piece1 - abs(audio1_dBFS)/2
            audio_piece2 = audio_piece2 - abs(audio2_dBFS)/2
            
            audio_piece = audio_piece1.overlay(audio_piece2)
   
            if ( audio1_dBFS < self.cutoff and audio2_dBFS < self.cutoff ):
                # or (audio1_dBFS > self.cutoff and audio2_dBFS > self.cutoff):
                higher_sound.append([time,2,audio_piece]) #video 3 

            elif abs(audio1_dBFS - audio2_dBFS) < self.cutoff_video3:
                higher_sound.append([time,2,audio_piece]) #video 3           
                
            elif audio1_dBFS > audio2_dBFS: #This is ok, it goes from -inf to 0 
                higher_sound.append([time,0,audio_piece]) #video 1

            else:
                higher_sound.append([time,1,audio_piece]) #video 2
                    
            if time + time_difference > audio_duration:
                time_difference = audio_duration - time
            time += time_difference
            
            if first_iteration == True:
                final_audio = audio_piece
                first_iteration = False
            else:
                final_audio  = final_audio + audio_piece
                
        return higher_sound,final_audio
    
    def get_video_sound_map(self):
            
        audio_file1 = self.video1.audio_file
        audio_file2 = self.video2.audio_file
            
        audio_duration = ( lambda x: min(x) )([audio_file1.duration_seconds, \
                                               audio_file2.duration_seconds])        
        audio_duration *= self.convert_time
        
        audio_duration = int(audio_duration)
        
        self.audio_duration = audio_duration
        
        self.higher_sound,final_audio = self.get_highest_sound_map(audio_file1,audio_file2,audio_duration,\
                              self.resolution,self.volume_reduction_factor)
        return final_audio

    def concat_video_by_sound(self, final_name = 'final_video.mp4',progress=False):
        previous_time = 0
        
        final_audio = self.get_video_sound_map()
        
        concatenate_clips = []
        
        try:
            video3_file = self.video3.video_file
        except AttributeError:
            video3_file = False
        
        videos = (self.video1.video_file,self.video2.video_file,video3_file)
        
        total_time = self.higher_sound[-1][0] / self.convert_time
        
        subtract_time = False
        merge_cells = False
    
        for i in range(len(self.higher_sound)):
            
            clip = self.higher_sound[i]
            
            if i < len(self.higher_sound) - 1:
                print("HERE",i,len(self.higher_sound))
                next_video = self.higher_sound[i + 1][1]
            else:
                next_video = False
            
            current_time = clip[0]
            
            if previous_time != current_time:
                
                if merge_cells == False:
                    ti = previous_time / self.convert_time
                tf = current_time / self.convert_time
                
                if subtract_time == True:
                    ti += self.change_time / self.convert_time
                    subtract_time = False
                
                if next_video != False:
                    if next_video != clip[1]:
                        tf += self.change_time / self.convert_time
                        subtract_time = True
                
                if tf <= ti:
                    merge_cells = True
                    continue
                else:
                    merge_cells = False
                
                if progress != False:
                    percentage = int( 100 * tf / total_time )
                    if percentage != 0:
                       percentage -= 1
                    progress(percentage)
                
                print('Video',clip[1]+1,'ti=',ti,'tf=',tf,'dBFS=',clip[2],\
                      int( 100 * tf / total_time ))
                         
                video_i = videos[clip[1]]
                
                if video_i == False:
                    continue
                
                subclip = video_i.subclip(ti,tf)
                
                concatenate_clips.append(subclip)
                
            previous_time = current_time
        
        
        final_video = me.concatenate_videoclips(concatenate_clips,method='compose')
        max_fps = max(clip.fps for clip in concatenate_clips)
        

        print("save final video",final_video.duration,current_time)
        final_video_obj = video( video_file = final_video )
        final_video_obj.change_audio( final_audio )
        
        final_video_name = self.path + final_name
        
        return final_video_name,final_video_obj,max_fps
        
    def normalize_audio(self, inputSound,targetDBFS):
        targetSound = pd.AudioSegment.from_wav(inputSound)
        changeInDBFS = targetDBFS - targetSound.dBFS
        targetSound.apply_gain(changeInDBFS)
        return targetSound
    
    def get_max_audio(self,inputSound,sliceSize):
        size = int(sliceSize * self.convert_time)
        audio = pd.AudioSegment.from_wav(inputSound)
        return max(chunk.dBFS for chunk in make_chunks(audio, size))
    
