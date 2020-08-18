import image, sensor, time
from machine import I2C
from modules import *


#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
# lcd.mirror(1)

dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
sensor_width = dev.width()
sensor_height = dev.height()

 #img = image.Image(size=(32,32))
 #img = img.to_grayscale()

temperature = []
while 1:
    try:
        temperature = dev.temperature()
        min, max, min_pos, max_pos = dev.min_max()
        img = dev.to_image(min, max)
        # print(temperature)
        print("max:", max)
        del img
        # print(clock.fps())
    except Exception as e:
        print(e)
