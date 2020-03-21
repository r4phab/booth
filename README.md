# Raspberry Booth

Based on https://github.com/RaspberryPiFoundation/jam-photobooth

## Requirements

Hardware:

- Raspberry Pi (any model with a camera port)
- Raspberry Pi camera module
- Any kind of standard GPIO push button ([arcade button](https://www.modmypi.com/raspberry-pi/sensors-1061/buttons-and-switches-1098/arcade-button-30mm-translucent-red)
with [quick-connect wire](https://www.modmypi.com/raspberry-pi/sensors-1061/buttons-and-switches-1098/arcade-button-quick-connect-wires-set-of-10-pairs)
reccomended)

Software:

- Picamera
- GPIO Zero

## Manual installation

• Download Raspbian Desktop :

    https://downloads.raspberrypi.org/raspbian_full_latest
 
• Install Raspbian to SD CARD :

    https://www.raspberrypi.org/documentation/installation/installing-images/

• Connect the camera module, wire your button to GPIO14 and insert the SD card.

• Power on the PI

• Enable the camera module with Raspi-config

    raspi-config
    
• Reboot.

    telinit 6

• Install the requirements:

    sudo apt update
    sudo apt install python3-gpiozero python3-picamera python3-pip git -y
    sudo pip3 install twython --upgrade

• Git clone this repository:

    git clone https://github.com/r4phab/booth

• Enter the project directory and run the photobooth script:

    python3 photobooth.py

• You should see an image preview appear, and the message:

    Ready!
    Press the button to start...

• Now use the button to progress to the next step, and continue.

• The application saves the photos in the `Pictures` folder at
`/home/pi/Pictures`.

• To make the program run on boot, add the following entry using `crontab -e`:

    @reboot python3 /home/pi/jam-photobooth/photobooth.py &
    
## Languages

Simply edit `text.py`, which contains dictionaries of the strings used as camera
text annotations, and add a copy of the English language dictionary `text_en`
below, renaming it as appropriate. Then replace the dictionary values (right
hand side) with the translated equivalents, leaving the keys (left hand side)
the same.

**Please note that the camera firmware does not support non-ASCII characters.**

To select a language, edit the following line in `photobooth.py`:

    python
    text = get_text(language='en')

Current language support:

- English - `en`
- German (Deutsche) - `de`
- French (Français) - `fr`
- Spanish (Español) - `es`
- Welsh (Cymraeg) - `cy`

## Modifications

Feel free to edit the code to your own specification. Note that the
`JamPiCamera` class is a slightly modified version of `PiCamera` (as you can
see in `jam_picamera.py`).

You may wish to rotate your picture around 180 degrees if your camera is
upside-down. Simply add `camera.rotation = 180` after `camera = JamPicamera()`.
