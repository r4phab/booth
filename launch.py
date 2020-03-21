from jam_picamera import JamPiCamera
from text import get_text
from gpiozero import Button
from time import sleep

camera = JamPiCamera()
camera.rotation = 30
button = Button(14, hold_time=5)

text = get_text(language='en')

camera.resolution = (1024, 768)
camera.annotate_text_size = 70
camera.start_preview()

def quit():
    camera.close()

def countdown(n):
    for i in reversed(range(n)):
        camera.annotate_text = '{}...'.format(i + 1)
        sleep(1)
    camera.annotate_text = None

def capture_photos(n):
    """
    Capture n photos in sequence and return a list of file paths
    """
    photos = []
    for pic in range(n):
        camera.annotate_text = text['photo number'].format(pic + 1, n)
        sleep(1)
        camera.annotate_text = text['press to capture']
        button.wait_for_press()
        button.wait_for_release()
        sleep(1)
        countdown(3)
        photo = camera.capture()
        photos.append(photo)
    return photos

button.when_held = quit

while True:
    camera.annotate_text = text['ready']
    button.wait_for_press()
    photos = capture_photos(4)
    camera.annotate_text = None
