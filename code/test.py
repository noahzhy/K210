import os, image, time
import KPU as kpu

md = kpu.load(0x400000)
kpu.set_outputs(md, 0, 1, 3, 1)
img = image.Image("/sd/3.jpg")
print(img)
#img = img.rgb_to_grayscale()
img.pix_to_ai()
a = kpu.forward(md, img)
fmap = kpu.get_output(md, 0)
print("fmap", fmap[:])

#print(os.listdir())

