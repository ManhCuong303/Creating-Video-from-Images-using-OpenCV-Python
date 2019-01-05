from PIL import Image
import cv2
import numpy as np
import json
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import moviepy.editor as mpe
from moviepy.video.tools.subtitles import SubtitlesClip,TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

Data = [
    [5, u'Fractal', u'Itvara', 'minimix', u'./img3/1.jpg'],
    [5, u'Case & Point', u'Error Code', 'minimix', u'./img3/2.jpg'],
    [5, u'Excision & Pegboard Nerds', u'Bring the Madness (Noisestorm Remix) [feat. Mayor Apeshit]', 'minimix',
     u'./img3/3.jpg'],
    [10, u'Nitro Fun', u'Final Boss', 'minimix', u'./img3/4.jpg'],
    [5, u'Astronaut', u'Quantum (Virtual Riot Remix)', 'minimix', u'./img3/5.jpg'],
    [5, u'Fractal', u'Contact', 'minimix', u'./img3/6.jpg']]

FPS = 60  # Sets the FPS of the entire video
currentFrame = 0
timeAllFrame = 0
startFrame = 0
imgFrame = 0
alphaT = FPS * 1.0
nameVideo = "slideshow.avi"
nameVideo2 = 'final_cut.mp4'
nameVideo3 = 'finalSUB.mp4'




def EffVideo(NameVideo):
    #add music to video
    videoclip = VideoFileClip(NameVideo)
    background_music = mpe.AudioFileClip('TakeMeHandRem.mp3')
    new_clip = videoclip.set_audio(background_music)

    # add sub to video
    generator = lambda txt: TextClip(txt, font='Georgia-Regular',fontsize=50, color='white', bg_color='black')
    sub = SubtitlesClip("sub.srt", generator)
    final = CompositeVideoClip([new_clip, sub])

    # concat intro to video
    clip1 = VideoFileClip("intro.mp4")
    final_clip = concatenate_videoclips([clip1, final], method="compose")
    final_clip.write_videofile("FullVideoHD.mp4")


for i in xrange(0, len(Data)):
    timeAllFrame = timeAllFrame + Data[i][0]
for i in xrange(0, len(Data)):
    Data[i][0] = Data[i][0] * FPS + imgFrame
    imgFrame = Data[i][0]

im1 = Image.open(Data[0][4])
im1 = im1.resize((2000, 1500))

height, width, layers = np.array(im1).shape  # Get some stats on the image file to create the video with
video = cv2.VideoWriter(nameVideo, cv2.VideoWriter_fourcc(*'DIVX'), FPS, (width, height), True)
imall = im1;
i = 0
z = 0

for currentData in Data:
    img1 = Image.open(currentData[4])
    img1 = img1.resize((2000, 1500))
    nt = currentData[0]
    for x in xrange(z, nt + 1):
        print '=>>', x, '<<='
        video.write(cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR))
    z = nt + 1
    if i < len(Data) - 1:

        nt = float(2 * FPS)
        img2 = Image.open(Data[i + 1][4])
        img2 = img2.resize((2000, 1500))
        for x in xrange(0, 2 * FPS + 1):
            al = x / (nt + 1)
            images1And2 = Image.blend(img1, img2, float(al))
            video.write(cv2.cvtColor(np.array(images1And2), cv2.COLOR_RGB2BGR))
    i += 1;

video.release()
EffVideo(nameVideo)


