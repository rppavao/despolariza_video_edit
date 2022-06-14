# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:48:38 2022

@author: Acer
"""
import moviepy.editor as me
import wave as wv
import pydub as pd
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

class video:
    def __init__(self,video_name='',path='',video_file=False,audio_name=''):
        
        self.path = path
        self.video_name = video_name
        if video_name != '':        
            self.video_file = me.VideoFileClip(path + video_name)       
        elif video_file != False:
            self.video_file = video_file
        
        if audio_name == '':
            self.audio_file = self.video_file.audio
        else:
            self.upload_audio(audio_name)
         
    def concatenate(self,other,name = "concat_video",save=True):
        
        result_video = video(name,self.path)
        result_video.video_file = me.concatenate_videoclips([self.video_file, \
                                                          other.video_file],method='compose')
        result_video.audio_file = result_video.video_file.audio
        
        if save == True:
            result_video.save_video()
        
        return result_video
    
    def save_video(self,new_name = ''):
        if new_name != '':
            self.name =  new_name
        
        self.video_file.write_videofile(self.path + self.name, fps=120, codec="mpeg4")
        self.save_audio(new_name)
        
        
    def save_audio(self,new_name=''):
        return
        if new_name != '':
           self.name =  new_name
    
        audio_name = self.path + self.name[:len(self.name)-4] + '.wav'
        
        self.audio_file.export(audio_name, format="wav")
    
    def upload_audio(self,audio_file_name):
        input_audio = pd.AudioSegment.from_wav(self.path + audio_file_name)
        self.change_audio(input_audio)         
    
    def change_audio(self,new_audio_file):
        self.audio_file = new_audio_file    
        return
    
        temp_name = self.path+"temp_audio.wav"
        
        video_duration = self.video_file.duration
        
        if new_audio_file.duration_seconds > video_duration:
            new_audio_file = new_audio_file[:video_duration * 1000]
        else:
            time_diference = video_duration - new_audio_file.duration_seconds
            second_of_silence = pd.AudioSegment.silent(duration=time_diference * 1000) # or be explicit
            new_audio_file += second_of_silence
        
        new_audio_file.export(temp_name, format="wav")
        input_audio = me.AudioFileClip(temp_name)
        
        self.audio_file = input_audio
        self.video_file = self.video_file.set_audio(input_audio)
        
        input_audio.close()
        
        os.remove(temp_name)
        
class edit_tools:
    def __init__(self,video1,video2,path='',parameters=(0,0,0)):
        self.path = path
        self.higher_sound = []
        self.video1 = video1
        self.video2 = video2
#        self.video3 = video3
        self.cutoff = parameters[0]
        self.convert_time = 1000 #seconds -> miliseconds
        self.resolution = parameters[1] * self.convert_time
        self.volume_reduction_factor = parameters[2]
    
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
        
            # if audio_piece1 < self.cutoff and audio_piece1 < self.cutoff:
            #     video_id = 3
            #     audio_piece1 -= self.volume_reduction_factor
            #     audio_piece2 -= self.volume_reduction_factor
            
            if audio_piece1.dBFS > audio_piece2.dBFS: #This is ok, it goes from -inf to 0
                higher_sound.append([time,1])
                if volume_reduction_factor == 0:
                    audio_piece2 = 0
                else:
                    audio_piece2 -= volume_reduction_factor
            else:
                higher_sound.append([time,2])
                if volume_reduction_factor == 0:
                    audio_piece1 = 0
                else:
                    audio_piece1 -= volume_reduction_factor
                    
            # print('>',time + time_difference,time_difference,audio_duration)
            if time + time_difference > audio_duration:
                time_difference = audio_duration - time
            time += time_difference
            
            if first_iteration == True:
                final_audio = audio_piece1 + audio_piece2
                first_iteration = False
            else:
                final_audio = final_audio + audio_piece1 + audio_piece2
        return higher_sound,final_audio
    
    def get_video_sound_map(self):
            
        audio_file1 = self.video1.audio_file
        audio_file2 = self.video2.audio_file
            
        audio_duration = ( lambda x: max(x) )([audio_file1.duration_seconds, \
                                               audio_file2.duration_seconds])        
        audio_duration *= self.convert_time
        
        audio_duration = int(audio_duration)
        
        self.audio_duration = audio_duration
        
        self.higher_sound,final_audio = self.get_highest_sound_map(audio_file1,audio_file2,audio_duration,\
                              self.resolution,self.volume_reduction_factor)
        return final_audio

    def concat_video_by_sound(self):
        previous_time = 0
        
        final_audio = self.get_video_sound_map()
        
        concatenate_clips = []
        
        temp_path = "D:/GoogleDrive/Despolariza/despolariza_video_edit/temp/"    
 
        for i in self.higher_sound:
            
            current_time = i[0]
            
            if i[1] == 1:
                clip_name = self.video1.path + self.video1.video_name
            elif i[1] == 2:
                clip_name = self.video2.path + self.video2.video_name
            # else:
            #     clip_name = self.video3.path + self.video3.video_name
            if previous_time != current_time:
                
                print(i[1],clip_name)
                
                temp_name = temp_path + "subclip" + str(int( current_time / self.convert_time )) + ".mp4"
                
                subclip = ffmpeg_extract_subclip(clip_name, previous_time / self.convert_time , \
                                                 current_time / self.convert_time \
                                                     , targetname=temp_name)
            
                subclip_obj = video(temp_name)
          
                concatenate_clips.append(subclip_obj.video_file)
            
                print("\n>>Time interval:",int(previous_time),'-',int(current_time),\
                      ' Total time:',int(self.audio_duration))
            
            previous_time = current_time
            
        final_video = me.concatenate_videoclips(concatenate_clips)    
        print("save final video",final_video.duration,current_time)
        final_video_obj = video( video_file = final_video)
        final_video_obj.change_audio( final_audio )
        final_video_obj.save_video("final_video.mp4")
        # try:
        #     final_video.write_videofile("final_video.mp4", codec="mpeg4")
        # except IndexError:
        #     # Short by one frame, so get rid on the last frame:
        #     final_video = final_video.subclip(t_end=(final_video.duration - 1.0/final_video.fps))
        #     final_video.write_videofile("final_video.mp4", codec="mpeg4")        
            
        
#This part is just for testing


name = "Video_sound3.mp4"

path = "D:/GoogleDrive/Despolariza/"    


video_test1 = video(name,path)


video_test1.upload_audio("sound3.wav")

#concat_video_by_sound

name = "Video_sound4.mp4"

video_test2 = video(name,path)

video_test2.upload_audio("sound4.wav")

obj_tools = edit_tools(video_test1,video_test2,path,(0,10,0))

obj_tools.concat_video_by_sound()

