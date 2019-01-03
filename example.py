from PIL import Image
import cv2
import numpy as np
import json

songData = [
    [50, u'Fractal', u'Itvara', 'minimix', u'./img/1.jpg'],
    [40, u'Case & Point', u'Error Code', 'minimix', u'./img/2.jpg'],
    [30, u'Excision & Pegboard Nerds', u'Bring the Madness (Noisestorm Remix) [feat. Mayor Apeshit]', 'minimix',
     u'./img/3.jpg'],
    [20, u'Nitro Fun', u'Final Boss', 'minimix', u'./img/4.jpg'],
    [10, u'Astronaut', u'Quantum (Virtual Riot Remix)', 'minimix', u'./img/5.jpg'],
    [0, u'Fractal', u'Contact', 'minimix', u'./img/6.jpg']]

FPS = 30  # Sets the FPS of the entire video
currentFrame = 0  # The animation hasn't moved yet, so we're going to leave it as zero
startFrame = 0  # The animation of the "next" image starts at "startFrame", at most
trailingSeconds = 5  # Sets the amount of time we give our last image (in seconds)
blendingDuration = 2.0  # Sets the amount of time that each transition should last for
# This could be more dynamic, but for now, a constant transition period is chosen
blendingStart = 10  # Sets the time in which the image starts blending before songFile

for i in songData:
    i[0] = i[0] * FPS  # Makes it so that iterating frame-by-frame will result in properly timed slideshows
im1 = Image.open(songData[-1][4])  # Load the image in
im2 = im1  # Define a second image to force a global variable to be created


current = songData[-1][4]  # We're going to let the script know the location of the current image's location
previous = current  # And this is to force/declare a global variable

height, width, layers = np.array(im1).shape  # Get some stats on the image file to create the video with
video = cv2.VideoWriter("slideshow.avi",cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height), True)

while currentFrame < songData[0][0] + FPS * 60 * trailingSeconds:  # RHS defines the limit of the slideshow
    for i in songData:  # Loop through each image timing
        if currentFrame >= i[0] - (blendingStart * FPS):  # If the image timing happens to be for the
            # current image, the continue on...
            # (Notice how songData is reversed)
            # The print statement adds some verbosity to the program
            print str(currentFrame) + " - " + str(i[0] - (blendingStart * FPS)) + " - " + i[2]
            if not current == i[4]:  # Check if the image file has changed
                previous = current  # We'd want the transition to start if the file has changed
                current = i[4]
                startFrame = i[0] - (blendingStart * FPS)
                # The two images in question for the blending is loaded in
                im1 = Image.open(previous)
                im2 = Image.open(current)
            break
    # See: http://blog.extramaster.net/2015/07/python-pil-to-mp4.html for the part below
    diff = Image.blend(im1, im2, min(1.0, (currentFrame - startFrame) / float(FPS) / blendingDuration))
    video.write(cv2.cvtColor(np.array(diff), cv2.COLOR_RGB2BGR))

    currentFrame += 1  # Next frame

# At this point, we'll assume that the slideshow has completed generating, and we want to close everything off to prevent a corrupted output.
video.release()