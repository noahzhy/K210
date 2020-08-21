import _thread, lcd, sensor
import time

lcd.init()
sensor.reset()
sensor.set_vflip(True)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

def func(name):
    while 1:
        print("hello {}".format(name))
        time.sleep(1)

_thread.start_new_thread(func,("1",))
_thread.start_new_thread(func,("2",))


def run():
    while 1:
        img = sensor.snapshot()
        lcd.display(img)
        pass


if __name__ == "__main__":
    run()
