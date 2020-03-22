from ftplib import FTP
from boothCamera import BoothCamera
from text import get_text
from time import sleep
import RPi.GPIO as GPIO
from PIL import Image
import os

BUTTON_PIN  = 21
LED_PIN = 16 #connected to external 12v.
buttonEvent = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = BoothCamera()
camera.rotation = 30

text = get_text(language='en')

camera.resolution = (1024, 768)
camera.start()

#button.when_held = quit

def state_start():
    camera.updateScreen("screen1")
    GPIO.setup(LED_PIN, GPIO.IN)

def play():
    camera.hideScreen()
    camera.updateOverlay("countdown3", 200)
    sleep(1)
    camera.updateOverlay("countdown2", 200)
    sleep(1)
    camera.updateOverlay("countdown1", 200)
    sleep(1)
    camera.updateOverlay("overlay", 50)
    sleep(1)
    photo = camera.capture()
    camera.updateScreen("loading")
    Image.alpha_composite(Image.open(photo).convert('RGBA'), Image.open(os.path.join(os.path.dirname(__file__), 'img/overlay.png')).convert('RGBA')).save(photo)

    ftp = FTP('159.89.15.202')
    ftp.login('userFtp', '$*M"8_S2P&q%cGb6')
    ftp.cwd("/var/www/html/www.marie-raphael.fr/images/booth")
    ftp.storbinary('STOR ' + camera.generateName(), open(photo, 'rb'))
    ftp.quit()

    camera.updateScreenWithImg("screenend", photo)
    sleep(20)

def onButtonPress():
    play()
    state_start()

state_start()

while True:
    #camera.annotate_text = text['ready']
    input_state = GPIO.input(BUTTON_PIN)
    if input_state == True :
        if buttonEvent == False :
            buttonEvent = True
            onButtonPress()
    else :
        if buttonEvent == True :
            buttonEvent = False
           #onButtonDePress()
