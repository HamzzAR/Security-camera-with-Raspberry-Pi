"""
This function takes a picture, stamps the picture
with current date&time and saves it in a specific dir
with a specific name. I call this fuction from the main.
"""

import picamera
from datetime import datetime
from subprocess import call

def takepic():
    fileName = "/home/pi/Desktop/CameraProject/pics/"

    currentTime = datetime.now()
    picTime = currentTime.strftime("%d/%m/%Y-%H:%M:%S")
    picName = "newPic.jpg"
    comleteFilePath = fileName + picName


    #setup the camera
    print('About to take a pictue..')
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture(comleteFilePath)
        print('Picture taken.')

    #create our stamp variable
    print('About to timestamp our picture.')
    timestampmsg = currentTime.strftime("%d/%m/%Y-%H:%M:%S")

    #create timestamp command
    timestampCommand = "/usr/bin/convert " + comleteFilePath + " -pointsize 32 \
    -fill red -annotate +900+695 '" + timestampmsg + "' " + comleteFilePath

    #execute our command
    call([timestampCommand], shell=True)
    print('Picture has been timestamped.')


