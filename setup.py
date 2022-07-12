# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 11:20:36 2022

@author: Rafael Pavão
"""

import os
from sys import platform

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

if platform == 'win32':
    commands = ('','python get-pip.py','pip install moviepy','pip install pydub',"pip install pyqt5",\
                "K-Lite_Codec_Pack_1710_Basic.exe")
else:
    commands = ('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py','python3 get-pip.py', \
                'pip install moviepy','pip install pydub',"brew install pyqt",\
                    "K-Lite_Codec_Pack_1710_Basic.exe") 

print('\nSetup will start')

# print('\n>> Getting pip file')
# urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
# os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')

print('\n>> Installing pip')
if platform != 'win32':
    os.system(commands[0])
os.system(commands[1])

print('\n>> Installing Moviepy')
os.system(commands[2])

print('\n>> Installing pydub')
os.system(commands[3])

print('\n>> Installing PyQT5')
os.system(commands[4])

print('\n>> Installing K-Lite Codec')
os.system(commands[5])

print('\nSetup completed!')