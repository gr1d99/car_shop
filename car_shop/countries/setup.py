import sys
import os


def country_file_path():
    countries_file = '%scountries.txt' % os.path.sep
    this_mod = sys.modules['car_shop'].countries
    path = this_mod.__path__
    file_path = path[0] + countries_file
    if os.path.isfile(file_path) is False:
        f = open(file_path, 'w')
        f.close()
    return file_path
