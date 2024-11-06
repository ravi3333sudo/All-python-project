#install; ImageMagick
from moviepy.editor import *

clip =VideoFileClip("video.mkv").subclip(0,10)

txt_clip =TextClip("Ravi Razz",fontsize=50,color="Brown")
txt_clip = txt_clip.set_position("Top").set_duration(10)

video =CompositeVideoClip([clip,txt_clip])

video.write_videofile("test.mp4")