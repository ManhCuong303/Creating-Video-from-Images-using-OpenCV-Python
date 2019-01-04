from PIL import Image
import cv2
import numpy as np
import json

Data = [
    [5, u'Fractal', u'Itvara', 'minimix', u'./img/1.jpg'],
    [5, u'Case & Point', u'Error Code', 'minimix', u'./img/2.jpg'],
    [5, u'Excision & Pegboard Nerds', u'Bring the Madness (Noisestorm Remix) [feat. Mayor Apeshit]', 'minimix',
     u'./img/3.jpg'],
    [10, u'Nitro Fun', u'Final Boss', 'minimix', u'./img/4.jpg'],
    [5, u'Astronaut', u'Quantum (Virtual Riot Remix)', 'minimix', u'./img/5.jpg'],
    [5, u'Fractal', u'Contact', 'minimix', u'./img/6.jpg']]


FPS = 10  # Sets the FPS of the entire video
currentFrame = 0
timeAllFrame = 0
startFrame = 0
imgFrame = 0
alphaT = FPS*1.0
for i in xrange(0,len(Data)):
    timeAllFrame = timeAllFrame + Data[i][0]
for i in xrange(0,len(Data)) :
    Data[i][0] = Data[i][0] * FPS + imgFrame
    imgFrame = Data[i][0]

im1 = Image.open(Data[0][4])

height, width, layers = np.array(im1).shape  # Get some stats on the image file to create the video with
video = cv2.VideoWriter("slideshow.avi", cv2.VideoWriter_fourcc(*'DIVX'), FPS, (width, height), True)
imall=im1;
i=0
for currentData in Data :
    img1 = Image.open( currentData[4])
    nt = currentData[0]
    for x in xrange(0,nt+1):
        print '',currentData[4]
        # images1And2 = Image.blend(im1, null, alphaT / FPS * 1.0)
        video.write(cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR))
    if i < len(Data)-1 :
        nt = 20.0
        img2 = Image.open(Data[i+1][4])
        # print 'asdad',Data[i+1][4]
        for x in xrange(0,21):
            al =  x/(nt+1)
            print currentData[4],'------------',Data[i+1][4],'------------', float(x/(nt+1))
            images1And2 = Image.blend(img1, img2,float(al))
            video.write(cv2.cvtColor(np.array(images1And2), cv2.COLOR_RGB2BGR))
    i+=1;
video.release()