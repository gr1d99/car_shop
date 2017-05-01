from car_shop.countries.setup import country_file_path
from car_shop.vehicles.setup import vehicles_file_path


class BaseClass(type):

    def __init__(cls, name, bases, clsdct):
        from car_shop.utils import output
        super(BaseClass, cls).__init__(name, bases, clsdct)
        cls_attribs = [
            'exit_keys', 'constant_price', 'get_vehicles_file',
            'get_countries_file', 'auto_check', 'banner', 'header',
            'footer', 'new_line',
        ]
        for attrib in cls_attribs:
            if not hasattr(cls, attrib):
                cls.constant_price = 10000
                cls.exit_keys = ['exit', 'Exit', 'EXIT', 'q', 'Q', 'quit', 'Quit', 'QUIT']
                cls.get_vehicles_file = vehicles_file_path()
                cls.get_countries_file = country_file_path()
                cls.banner = output.banner
                cls.header = output.header

    def __str__(self):
        return "%s object" % self.__name__

