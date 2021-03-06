import RPi.GPIO as gpio
import os
import time
from picamera import camera
import cv2
from PIL import Image

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.IN,pull_up_down=gpio.PUD_UP)
#cam = camera.PiCamera()
#cam.resolution = (1920,1080)
#cam.color_effects = (128, 128)
while True:
    print("Waiting for button")
    gpio.wait_for_edge(23, gpio.RISING)

    if os.path.exists("lock"):
        continue

    os.system("touch lock")
    os.system("./{0} {1} {2} {3} {4} {5} {6} {7}".format('a.out', *[0,0,0,0,0,0,1]))
    #cam.capture("imagem.jpg")
    start_time = time.time()
    os.system("raspistill -o imagem.jpg -cfx 128:128")
    im = Image.open('imagem.jpg')
    im = im.rotate(90, expand=1)
    im.save('imagem.jpg')
    print("Photo taken")

    print(time.time() - start_time)
    time.sleep(0.6)
