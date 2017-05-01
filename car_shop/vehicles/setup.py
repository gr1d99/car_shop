import sys
import os


def vehicles_file_path():
    vehicle_file = '%svehicles.txt' % os.path.sep
    this_mod = sys.modules['car_shop'].vehicles
    path = this_mod.__path__
    file_path = path[0] + vehicle_file
    if os.path.isfile(file_path) is False:
        f = open(file_path, 'w')
        f.close()
    return file_path
