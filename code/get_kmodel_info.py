import KPU as kpu

task = kpu.load(0x400000)
kpu.set_outputs(task, 0, 1,3,1)


info = kpu.netinfo(task)
layerbottom = info[-1]

print(info, layerbottom)
