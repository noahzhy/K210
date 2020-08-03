import sensor, image, utime


class time_machine:
    def __init__(self, _init=None):
        if _init:
            self._init = utime.mktime(_init)
        else:
            self._init = utime.mktime((2000, 1, 1, 0, 0, 0, 0, 0))
        print('[init]', 'time', utime.localtime(self._init))

    def get_date(self):
        now = utime.ticks_add(self._init, int(utime.ticks()/1000))
        date = utime.localtime(int(now))
        return "%02u/%02u/%02u" % (date[0], date[1], date[2])

    def get_time(self):
        now = utime.ticks_add(self._init, int(utime.ticks()/1000))
        _time = utime.localtime(int(now))
        return "%02u:%02u:%02u" % (_time[3], _time[4], _time[5])


if __name__ == "__main__":
    tm = time_machine((2020, 8, 2, 22, 46, 0, 0, 0))
    #tm = time_machine()

    while(True):
        print(tm.get_date(), tm.get_time())
        utime.sleep(3)
