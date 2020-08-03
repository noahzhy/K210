import socket, network, time
import lcd, image
from Maix import GPIO
from machine import UART
from fpioa_manager import fm, board_info

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
