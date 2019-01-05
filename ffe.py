from PIL import Image
import cv2
import numpy as np
import json
import glob, os


# file, ext = os.path.splitext(infile)
im = Image.open('./img3/4.jpg')
height, width, layers = np.array(im).shape  # Get some stats on the image file to create the video with
video = cv2.VideoWriter("60fps.avi", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height), True)
i = 0
while i <= 180.0:
    im = Image.open('./img3/4.jpg')
    im.crop((0, 0, 800, 600))
    im = im.rotate(i)
    # im.thumbnail(size)
    im = np.array(im)
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    video.write(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR))
    i += 0.4

video.release()
