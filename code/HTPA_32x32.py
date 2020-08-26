#import image, sensor, time, lcd, os
import lcd, os
from machine import I2C
from modules import htpa

print(os.listdir())

lcd.init()
lcd.draw_string(10, 10, "hello")
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.run(1)

# def save_img(img):
#     path = "/sd/img_{}.jpg".format(time.localtime())
#     img.save(path)
#     print(len(os.listdir()))


#def run():
    #dev = htpa(i2c=I2C.I2C0, scl_pin=12, sda_pin=11, i2c_freq=1000000)
    #sensor_width = dev.width()
    #sensor_height = dev.height()
    ##reg = dev.__write_reg(0x00d0, 15)
    ##reg = dev.__read_reg(0xd0)
    #print(reg, type(reg))

    #while True:
        #try:
            #dev.temperature()
            #min, max, min_pos, max_pos = dev.min_max()
            #if max > 6000:
                #continue
            #img = dev.to_image(min, max)
            ## save to SD card
            ## save_img(img)
            #lcd.display(img.resize(240,240))
        #except Exception as e:
            #print(e)


#if __name__ == "__main__":
    #run()
