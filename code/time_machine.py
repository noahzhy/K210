import sensor
import image
import utime


class time_machine:
    def __init__(self, _init=None):
        if not _init: _init = (2000, 1, 1, 0, 0, 0, 0, 0)
        self._init = utime.mktime(_init)
        print('[init]', 'time', utime.localtime(self._init))

    def get_datetime(self):
        now = utime.ticks_add(self._init, int(utime.ticks()/1000))
        date = utime.localtime(int(now))
        return "%02u/%02u/%02u %02u:%02u:%02u" % (date[0:6])

    def get_date(self):
        return self.get_datetime().split()[0]

    def get_time(self):
        return self.get_datetime().split()[1]


if __name__ == "__main__":
    tm = time_machine((2020, 8, 2, 22, 46, 0, 0, 0))
    # tm = time_machine()
    while(True):
        print(tm.get_datetime())
        utime.sleep(3)
