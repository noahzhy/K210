import image, sensor, lcd, socket, network, time
from Maix import GPIO
from machine import UART
from fpioa_manager import fm, board_info

lcd.init()
# clock = time.clock()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.skip_frames(30)


def connect_wifi(WIFI_SSID=None, WIFI_PASSWD=None):
    if not (WIFI_SSID and WIFI_PASSWD):
        WIFI_SSID = "317"
        WIFI_PASSWD = "hikorea317"

    uart = UART(UART.UART2, 921600, timeout=1000, read_buf_len=10240)
    nic = network.ESP8285(uart)
    err = 0

    while 1:
        try:
            nic.connect(WIFI_SSID, WIFI_PASSWD)
        except Exception:
            err += 1
            print("Connect AP failed, now try again")
            if err > 3:
                raise Exception("Conenct AP fail")
            continue
        break

    print(nic.ifconfig())
    return nic.isconnected()


def qr_detection(img):
    qrcodes = img.find_qrcodes()
    if len(qrcodes) > 0:
        content = qrcodes[0].payload()
        print(content)
        return content


while True:
    #clock.tick()
    img = sensor.snapshot()
    qrcodes = img.find_qrcodes()
    #fps = clock.fps()
    if len(qrcodes) > 0:
        #img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        print(qrcodes[0].payload())

    lcd.display(img)

#print(connect_wifi())
