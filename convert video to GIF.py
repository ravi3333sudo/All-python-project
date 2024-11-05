from moviepy.editor import *

video = VideoFileClip("video.mkv").subclip(00,5).rotate(180)
video.write_gif("test2.gif")