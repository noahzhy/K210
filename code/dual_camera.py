import sensor
import image
import lcd
import time

lcd.init()
sensor.binocular_reset()
sensor.shutdown(False)#选择sensor并初始化
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.shutdown(True)#选择sensor并初始化
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
while True:
    sensor.shutdown(False) #选择sensor
    img=sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)
    sensor.shutdown(True) #选择sensor
    img=sensor.snapshot()
    lcd.display(img)
    time.sleep_ms(100)
