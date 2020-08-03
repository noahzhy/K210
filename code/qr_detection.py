import image
import sensor
import lcd

lcd.init()
# lcd.rotation(1)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.skip_frames(30)


def qr_detection(img):
    qrcodes = img.find_qrcodes()
    if len(qrcodes) > 0:
        content = qrcodes[0].payload()
        print(content)
        return content


if __name__ == "__main__":
    while True:
        img = sensor.snapshot()
        qr_detection(img)
        lcd.display(img)
