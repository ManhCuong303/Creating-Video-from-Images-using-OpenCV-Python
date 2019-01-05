import cv2
import numpy as np
import os

from os.path import isfile, join

# Image Folder Path
path_folder = "./img2/"
# Width of slideshow
slideshow_width = 1500
# Height of slideshow
slideshow_height = 1000
# thoi gian chuyen anh
slideshow_trasnition_time = 0.5
# thoi hien thi anh
slideshow_img_time = 1
# Window Name
window_name = "Image Slide Show"
# Supoorted formats tuple
supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.dib', '.jpe', '.jp2', '.pgm', '.tiff', '.tif', '.ppm')
# Escape ASCII Keycode
esc_keycode = 27
# slide calibration
transit_slides = 10
# minimum weight
min_weight = 0
# maximum weight
max_weight = 1
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
def wait_key(time_seconds):
    # state False if no Esc key is pressed
    state = False
    # Check if any key is pressed. second multiplier for millisecond: 1000
    k = cv2.waitKey(int(time_seconds * 1000))
    # Check if ESC key is pressed. ASCII Keycode of ESC=27
    if k == esc_keycode:
        # Destroy Window
        cv2.destroyWindow(window_name)
        # state True if Esc key is pressed
        state = True
    # return state
    return state

def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    # for sorting the file names properly

    for i in range(len(files)):
        filename = pathIn + files[i]
        print 'sssssssssssssss',filename
        # reading each files
        img = cv2.imread(filename)
        img = load_img(filename, 1000, 500)
        height, width, layers = img.shape
        size = (width, height)

        cv2.imshow('asdasd',img)
        if wait_key(1):
            break
        print(filename)
        # inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


def main():
    pathIn = './img3/'
    pathOut = 'video.avi'
    fps = 0.5
    convert_frames_to_video(pathIn, pathOut, fps)


if __name__ == "__main__":
    main()