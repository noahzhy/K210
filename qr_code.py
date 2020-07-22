import image,sensor,lcd,time

clock = time.clock()

lcd.init()
#lcd.rotation(1)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(1)
sensor.skip_frames(30)

while True:
    #clock.tick()
    img = sensor.snapshot()
    qrcodes = img.find_qrcodes()
    #fps = clock.fps()
    if len(qrcodes) > 0:
        #img.draw_string(2,2, res[0].payload(), color=(0,128,0), scale=2)
        print(qrcodes[0].payload())

    lcd.display(img)
