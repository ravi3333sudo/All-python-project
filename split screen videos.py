from moviepy.editor import *

clip_1 =VideoFileClip("video.mkv").subclip(0,10)
clip_2 =VideoFileClip("video.mkv").subclip(10,20)
clip_3 =VideoFileClip("video.mkv").subclip(20,30)
clip_4 =VideoFileClip("video.mkv").subclip(40,40)

comb = clips_array([[clip_1,clip_2],
                    [clip_3,clip_4]])

comb.write_videofile("test.mp4")