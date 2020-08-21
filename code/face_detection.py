import sensor
import image
import lcd
import KPU as kpu


SINGLE_FACE_DETECTION = True

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

task = kpu.load(0x300000)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987,
          5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
kpu.init_yolo2(task, 0.4, 0.25, 5, anchor)

while True:
    img = sensor.snapshot()
    fd = kpu.run_yolo2(task, img)
    if fd:
        for i in fd:
            x, y, w, h = i.rect()
            print("face detected:", i.rect(), w*h)
            if w*h < 5000:
                break
            img.draw_rectangle(i.rect(), color=(0, 255, 0), thickness=3)
            if SINGLE_FACE_DETECTION:
                break

    lcd.display(img)

kpu.deinit(task)
