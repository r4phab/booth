from PIL import Image
from picamera import PiCamera
from time import gmtime, strftime
import os

screen = None
overlay = None

def _pad(resolution, width=32, height=16):
    # A little utility routine which pads the specified resolution
    # up to the nearest multiple of *width* and *height*; this is
    # needed because overlays require padding to the camera's
    # block size (32x16)
    return (
        ((resolution[0] + (width - 1)) // width) * width,
        ((resolution[1] + (height - 1)) // height) * height,
    )

def _gen_filename():
    """
    Generates a filename with a timestamp
    """
    filename = strftime("/home/pi/Pictures/photo-%d-%m %H:%M:%S.png", gmtime())
    return filename

class BoothCamera(PiCamera):
    def start(self):
        self.updateOverlay("overlay", 50)
        super(BoothCamera, self).start_preview(fullscreen=True)

    def showScreen(self):
        global screen
        screen.layer=4

    def hideScreen(self):
        global screen
        screen.layer=1

    def updateOverlay(self, img, alpha):
        pad = Image.new('RGB', _pad(self.resolution))
        pad.paste(Image.open(os.path.join(os.path.dirname(__file__), 'img/' + img + '.png')), (0, 0))
        global overlay
        if not overlay:
            overlay = self.add_overlay(pad.tobytes(), alpha=alpha, layer=3);
        else:
            overlay.alpha=alpha
            overlay.update(pad.tobytes())

    def updateScreen(self, img):
        pad = Image.new('RGB', _pad(self.resolution))
        pad.paste(Image.open(os.path.join(os.path.dirname(__file__), 'img/' + img + '.png')), (0, 0))
        global screen
        if not screen:
            screen = self.add_overlay(pad.tobytes(), layer=1);
        else:
            screen.update(pad.tobytes())

        self.showScreen()

    def updateScreenWithImg(self, img, capture):
        pad = Image.new('RGB', _pad(self.resolution))
        pad.paste(Image.open(os.path.join(os.path.dirname(__file__), 'img/' + img + '.png')), (0, 0))
        pad.paste(Image.open(capture).resize((600, 455), Image.ANTIALIAS), (212, 40))
        global screen
        if not screen:
            screen = self.add_overlay(pad.tobytes(), layer=1);
        else:
            screen.update(pad.tobytes())

        self.showScreen()

    def capture(self):
        output = _gen_filename()
        super(BoothCamera, self).capture(output)
        return output
