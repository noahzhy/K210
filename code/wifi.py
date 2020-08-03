import socket
import network
import time
import lcd
import image
from Maix import GPIO
from machine import UART
from fpioa_manager import fm, board_info


def connect_wifi(WIFI_SSID=None, WIFI_PASSWD=None):
    if WIFI_SSID or WIFI_PASSWD:
        # for new MaixGO board, if not, remove it
        fm.register(0, fm.fpioa.GPIOHS1, force=True)
        wifi_io0_en = GPIO(GPIO.GPIOHS1, GPIO.OUT)
        wifi_io0_en.value(0)

        # En ESP8285
        fm.register(8, fm.fpioa.GPIOHS0, force=True)
        wifi_en = GPIO(GPIO.GPIOHS0, GPIO.OUT)
        fm.register(board_info.WIFI_RX, fm.fpioa.UART2_TX, force=True)
        fm.register(board_info.WIFI_TX, fm.fpioa.UART2_RX, force=True)

    def wifi_enable(en):
        wifi_en.value(en)

    def wifi_reset():
        global uart
        wifi_enable(0)
        time.sleep_ms(200)
        wifi_enable(1)
        time.sleep(2)
        uart = UART(UART.UART2, 115200, timeout=1000, read_buf_len=4096)
        tmp = uart.read()
        uart.write("AT+UART_CUR=921600,8,1,0,0\r\n")
        print(uart.read())
        # important! baudrate too low or read_buf_len too small will loose data
        uart = UART(UART.UART2, 921600, timeout=1000, read_buf_len=10240)
        uart.write("AT\r\n")
        tmp = uart.read()
        print(tmp)
        if not tmp.endswith("OK\r\n"):
            print("reset fail")
            return None
        try:
            nic = network.ESP8285(uart)
        except Exception:
            return None
        return nic

    nic = wifi_reset()
    if not nic:
        raise Exception("WiFi init fail")

    nic = network.ESP8285(uart)
    err = 0

    while True:
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


if __name__ == "__main__":
    WIFI_SSID = "317"
    WIFI_PASSWD = "hikorea317"

    connect_wifi(WIFI_SSID, WIFI_PASSWD)
