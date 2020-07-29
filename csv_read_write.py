import sensor, image, time
import os


CSV_FILE = '/sd/attendance.csv'
MAIN_FILE = '/sd/main.py'


def csv_add():
    # os.remove(CSV_FILE)
    # os.remove(MAIN_FILE)
    # if not exist, create it
    if
    f = open(CSV_FILE, 'w+')
    f.write('datetime, employee_id, temperature, addition\n')
    f.write('안녕')
    f.close()

    with open(CSV_FILE, 'r') as f:
        res = f.readline()
        print(res)

    _list = os.listdir()
    print(_list)

csv_add()
