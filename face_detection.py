import sensor
import image
import lcd
import KPU as kpu

Single_Face_Detecion = True

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

task = kpu.load(0x300000)
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.718375, 9.01025)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

# info = kpu.netinfo(task)
# print(info)
# quit()

while True:
    img = sensor.snapshot()
    fd = kpu.run_yolo2(task, img)
    if fd:
        for i in fd:
            print("face detected:", i)
            a = img.draw_rectangle(i.rect(), color=(0,255,0), thickness=3)
            if Single_Face_Detecion:
                break
    
    a = lcd.display(img)

a = kpu.deinit(task)
