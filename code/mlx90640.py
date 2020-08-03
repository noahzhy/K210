import lcd, image, time
#import sensor
from machine import I2C
#import busio
#import pyb


i2c = I2C(I2C.I2C0, freq=100000, sda=6, scl=7)
devices = i2c.scan()
print(devices)
data = i2c.readfrom(devices[0], 768)
print(data)
#lcd.init()
#lcd.draw_string(100, 100, "{}".format(devices), lcd.GREEN, lcd.BLACK)

#lcd_w = 320
#lcd_h = 240

#edge = (-1,-1,-1,-1,8,-1,-1,-1,-1)

#offset_x = 0
#offset_y = 50
#zoom = 2
#rotate = 0

#lcd.init(type=2, freq=20000000)
#lcd.rotation(1)
#dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
#sensor_width = 32
#sensor_height = 24
#img = image.Image(size=(32,24))
## img = img.to_grayscale()
#clock = time.clock()
#while 1:
    #clock.tick()
    #try:
        #temperature = dev.temperature()
        #print(temperature)
