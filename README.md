Intervalometer
=========

A simple camera intervalometer/remote shutter using a Raspberry Pi inspired by [this video]

Features
--------
  - Set a delay before the first shot
  - Select how long the shot it's going to take (for exposures > 1 seconds)
  - Set the time between each shot
  - Set a length for video
  - Set a maximum number of shots to take


Version
----

1.0

Tech
-----------

The Intervalometer (as of now) requires the following:

* Raspberry Pi Rev 2.0 Model B
* SD Card, 4GB with Raspbian installed
* [Adafruit's 16x2 LCD Character Display] or any similar 16x2 LCD Character Display
* [Adafruit's PiCobbler] (or you can make yor own)
* 6 buttons
* 

Installation
--------------

```sh
git clone https://github.com/omarowns/Intervalometer.git intervalometer
cd intervalometer
chmod +x menu.py
sudo ./menu.py
```

##### Configuration
If you want to use GPIOs other than the ones established, you may need to edit the lines where the buttons are declared as well as the LCD initialization.


License
----

View LICENCE file


[this video]:http://www.youtube.com/watch?v=co8nnnvP6oM
[Adafruit's 16x2 LCD Character Display]:http://www.adafruit.com/products/181
[Adafruit's PiCobbler]:http://www.adafruit.com/products/914
