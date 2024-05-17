from datetime import timedelta
from PIL import Image

import numpy
import time
import cv2

FPS = 25

elaina = Image.open("elaina_confused.png")
black = Image.new("RGB", (1920, 1080), (0, 0, 0))
video = cv2.VideoWriter("elaina-san_dvd_bouncing_while_shocked_for_10_hours.mp4", cv2.VideoWriter_fourcc(*'mp4v'), FPS, (1920, 1080))
num_frames = FPS * 60 * 60 * 10

position = [100, 100]
velocity = [10, 10]

start = time.time()
percent = -1
for frame in range(1, num_frames):
    position = [position[0] + velocity[0], position[1] + velocity[1]]

    velocity[0] *= {0: 1, 1: -1}[position[0] <= 0 or position[0] >= 1920 - elaina.size[0]]
    velocity[1] *= {0: 1, 1: -1}[position[1] <= 0 or position[1] >= 1080 - elaina.size[1]]

    im = black.copy()
    im.paste(elaina, position)
    video.write(numpy.array(im))
    if frame % (FPS * 10) == 0:
        print(f"{int(frame/num_frames * 100)}% - {str(timedelta(seconds = int((time.time() - start) * ((num_frames - frame) / frame))))} remaining", end="\r")

video.release()