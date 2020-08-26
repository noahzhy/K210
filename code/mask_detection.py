import image, sensor, time, lcd, os
from machine import I2C
from modules import htpa
import KPU as kpu

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

dev = htpa(i2c=I2C.I2C0, scl_pin=7, sda_pin=6, i2c_freq=1000000)
sensor_width = dev.width()
sensor_height = dev.height()

md = kpu.load(0x400000)
kpu.set_outputs(md, 0, 1, 3, 1)

def save_img(img):
    path = "/sd/img_{}.jpg".format(time.localtime())
    img.save(path)
    print(len(os.listdir()))


def run():
    label_text = ""
    while True:
        try:
            dev.temperature()
            min, max, min_pos, max_pos = dev.min_max()
            if max > 6000:
                continue
            img = dev.to_image(min, max)
            img.pix_to_ai()
            a = kpu.forward(md, img)
            fmap = kpu.get_output(md, 0)
            masked, no_mask, fake = fmap[:]
            print(fmap[:])
            if masked >= 0.8:
                label_text = "Masked"
            elif no_mask >= 0.9:
                label_text = "No Mask"
            elif fake >= 0.8:
                label_text = "Fake"
            img = img.resize(240,240)
            img.draw_string(10, 10, label_text, color=(0x00, 0xff, 0x00), scale=2)
            # save to SD card
            #save_img(img)
            lcd.display(img)
            #time.sleep(1)
        except Exception as e:
            print(e)

    a = kpu.deinit(md)

if __name__ == "__main__":
    run()
