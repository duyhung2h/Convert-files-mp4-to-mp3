# pip install moviepy

import os
from moviepy.editor import *
rootPath = os.path.abspath(os.curdir) + "/convert folder/tot intro/"
print(rootPath + "/convert folder/tot intro/")


for id in range (1, 7, 1):
    video = VideoFileClip(os.path.join("path","to", rootPath + str(id) + ".mp4" ))
    video.audio.write_audiofile(os.path.join("path","to", rootPath + str(id) + ".mp3" ))