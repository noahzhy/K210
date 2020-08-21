import image, sensor, time
from machine import I2C
from modules import htpa
#from Maix import FPIOA
#from fpioa_manager import fm

#fpioa = FPIOA()
#fpioa.set_function(20, fm.fpioa.I2C0_SCLK)
#fpioa.set_function(21, fm.fpioa.I2C0_SDA)
#fpioa.help()
import lcd

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
#lcd.mirror(1)

dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)

#dev = htpa(i2c=I2C.I2C0, scl_pin=30, sda_pin=31, i2c_freq=1152000)
#sensor_width = dev.width()
#sensor_height = dev.height()
sensor_width = 32
sensor_height = 32
 #img = image.Image(size=(32,32))
 #img = img.to_grayscale()

count = 0
temperature = []
while 1:
    #count += 1
    images = sensor.snapshot()
    try:
        #dev = htpa(i2c=I2C.I2C0, scl_pin=20, sda_pin=21, i2c_freq=1000000)
        #dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
        #temperature = dev.temperature()
        min, max, min_pos, max_pos = dev.min_max()
        #img = dev.to_image(min, max)
        #print(temperature)
        print("max:", max)
        lcd.display(images)
        #del img
        # print(clock.fps())
    except Exception as e:
        print(e)
