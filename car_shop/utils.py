from car_shop.app_settings import BANNER, HEADER


class Output(object):
    def __init__(self, banner, header):
        self.banner = banner
        self.header = header


def create_output(BANNER, HEADER):
    instance = Output(BANNER, HEADER)
    return instance


output = create_output(BANNER, HEADER)
