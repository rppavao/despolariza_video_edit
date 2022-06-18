# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 11:20:36 2022

@author: Rafael Pavão
"""

import os

try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

print('\nSetup will start')

print('\n>> Getting pip file')
# urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')

print('\n>> Installin pip')
os.system('python get-pip.py')

print('\n>> Installing Moviepy')
os.system('pip install moviepy')

print('\n>> Installing pydub')
os.system('pip install pydub')

print('\nSetup completed')