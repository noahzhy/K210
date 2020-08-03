import sensor, image, time
import uos


CSV_FILE = '/sd/attendance.csv'
MAIN_FILE = '/sd/main.py'

#uos.remove(CSV_FILE)
#uos.remove(MAIN_FILE)

class csv_file:
    def __init__(self, _path='/sd/attendance.csv'):
        self.path = _path
        try:
            uos.stat(self.path)
        except OSError:
            print("[Info]", "Not exist, create it and add header")
            with open(self.path, 'w+') as f:
                f.write('datetime, employee_id, temperature, addition\n')

    def add(self, dt, e_id, temp, addi=''):
        try:
            with open(self.path, 'a+') as f:
                f.write('{},{},{},{}\n'.format(dt, e_id, temp, addi))
        except OSError:
            print("[Warning]", "Attendance info add fail")

    def print_csv(self):
        with open(self.path, 'r') as f:
            for line in f.readlines():
                print(line.strip())


if __name__ == "__main__":
    print(uos.listdir())

    csv = csv_file(CSV_FILE)
    csv.add(1, 2, 3)
    csv.print_csv()
