from PIL import Image
import cv2
import numpy as np
import json
from moviepy.editor import *

Data = [
    [5, u'Fractal', u'Itvara', 'minimix', u'./img3/1.jpg'],
    [5, u'Case & Point', u'Error Code', 'minimix', u'./img3/2.jpg'],
    [5, u'Excision & Pegboard Nerds', u'Bring the Madness (Noisestorm Remix) [feat. Mayor Apeshit]', 'minimix',
     u'./img3/3.jpg'],
    [10, u'Nitro Fun', u'Final Boss', 'minimix', u'./img3/4.jpg'],
    [5, u'Astronaut', u'Quantum (Virtual Riot Remix)', 'minimix', u'./img3/5.jpg'],
    [5, u'Fractal', u'Contact', 'minimix', u'./img3/6.jpg']]

FPS = 10  # Sets the FPS of the entire video
currentFrame = 0
timeAllFrame = 0
startFrame = 0
imgFrame = 0
alphaT = FPS * 1.0


def load_img(pathImageRead, resizeWidth, resizeHeight):
    # Load an image
    # cv2.IMREAD_COLOR = Default flag for imread. Loads color image.
    # cv2.IMREAD_GRAYSCALE = Loads image as grayscale.
    # cv2.IMREAD_UNCHANGED = Loads image which have alpha channels.
    # cv2.IMREAD_ANYCOLOR = Loads image in any possible format
    # cv2.IMREAD_ANYDEPTH = Loads image in 16-bit/32-bit otherwise converts it to 8-bit
    _img_input = cv2.imread(pathImageRead, cv2.IMREAD_UNCHANGED)
    # Check if image is not empty
    if _img_input is not None:
        # Get read images height and width
        _img_height, _img_width = _img_input.shape[:2]

        # if image size is more than resize perform cv2.INTER_AREA interpolation otherwise cv2.INTER_LINEAR for zooming
        if _img_width > resizeWidth or _img_height > resizeHeight:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_LINEAR

        # perform the actual resizing of the image and show it
        _img_resized = cv2.resize(_img_input, (resizeWidth, resizeHeight), interpolation)
    else:
        # if image is empty
        _img_resized = _img_input
    # return the resized image
    return _img_resized


for i in xrange(0, len(Data)):
    timeAllFrame = timeAllFrame + Data[i][0]
for i in xrange(0, len(Data)):
    Data[i][0] = Data[i][0] * FPS + imgFrame
    imgFrame = Data[i][0]

im1 = Image.open(Data[0][4])
im1 = im1.resize((1000, 600))

height, width, layers = np.array(im1).shape  # Get some stats on the image file to create the video with
video = cv2.VideoWriter("slideshow.avi", cv2.VideoWriter_fourcc(*'DIVX'), FPS, (width, height), True)
imall = im1;
i = 0
z = 0

for currentData in Data:
    img1 = Image.open(currentData[4])
    img1 = img1.resize((1000, 600))
    nt = currentData[0]
    for x in xrange(z, nt + 1):
        video.write(cv2.cvtColor(np.array(img1), cv2.COLOR_RGB2BGR))
    z = nt + 1
    if i < len(Data) - 1:
        nt = float(2 * FPS)
        img2 = Image.open(Data[i + 1][4])
        img2 = img2.resize((1000, 600))
        for x in xrange(0, 2 * FPS + 1):
            al = x / (nt + 1)
            images1And2 = Image.blend(img1, img2, float(al))
            video.write(cv2.cvtColor(np.array(images1And2), cv2.COLOR_RGB2BGR))
    i += 1;

video.release()
