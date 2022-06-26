# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:20:14 2022

@author: Rafael Pavão
"""

import os

class directory:
    def __init__(self,in_directory=False):
        if in_directory == False:
            self.directory = os.getcwd().replace('\\','/')
        else:
            self.directory = in_directory
        self.directory_list = self.directory.split('/')
        self.subdirectory_list = []
        self.files_list = []
        
    def get_subdir_and_files(self):
        for obj in os.scandir(self.directory):
            if obj.is_dir():
                self.subdirectory_list.append(obj.path.replace('\\','/'))
            else:
                file = obj.path.split('\\')[-1]
                self.files_list.append(file)

        
                