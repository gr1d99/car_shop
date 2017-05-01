import sys
import six
from collections import OrderedDict
from .core.base import BaseClass


class Configuration(six.with_metaclass(BaseClass)):

    def __init__(self):
        if not self.get_vehicles_file or not self.get_countries_file:
            sys.exit(1)


class Country(Configuration):
    def __init__(self):
        super(Country, self).__init__()

    def existingCountries(self):
        previous_countries = open(self.get_countries_file, 'r').readlines()
        for cn in previous_countries:
            yield cn

    def show_countries(self):
        counter = 0
        print('COUNTRY LIST\n')
        for c in self.existingCountries():
            counter += 1
            print("Country no %s: %s\n\n" % (counter, c.strip('\n').capitalize()))

    def addCountry(self):
        prompt = True
        print("Enter country name then press ENTER Key to add another country\n\n")
        countries = []
        country_file = open(self.get_countries_file, 'a')
        existing = [country.split('\n')[0] for country in self.existingCountries()]

        while prompt:
            country = raw_input().lower().strip()
            if country not in self.exit_keys:
                if country is not '' and country not in existing and country not in countries:
                    countries.append(country)

            else:
                for country in countries:
                    data = '%(country)s%(sep)s' % dict(
                        country=country,
                        sep='\n'
                    )
                    country_file.write(data)
                country_file.close()
                print('\n\n')
                prompt = False


class Vehicle(Configuration):
    def __init__(self):
        super(Vehicle, self).__init__()

    def existingVehicles(self):
        previous_vehicles = open(self.get_vehicles_file, 'r').readlines()
        for vl in previous_vehicles:
            yield vl

    def show_vehicles(self):
        counter = 0
        print('VEHICLE LIST\n')
        for v in self.existingVehicles():
            counter += 1
            print("Vehicle no %s: %s\n" % (counter, v.capitalize()))

    def addVehicle(self):
        prompt = True
        print("Enter vehicle name then press ENTER Key to add another vehicle\n\n")
        vehicles = []
        vehicles_file = open(self.get_vehicles_file, 'a')
        existing = [vehicle.split('\n')[0] for vehicle in self.existingVehicles()]

        while prompt:
            vehicle = raw_input().lower().strip()
            if vehicle not in self.exit_keys:
                if vehicle is not '' and vehicle not in existing and vehicle not in vehicles:
                    vehicles.append(vehicle)

            else:
                for vehicle in vehicles:
                    data = '%(vehicle)s%(sep)s' % dict(
                        vehicle=vehicle,
                        sep='\n'
                    )
                    vehicles_file.write(data)
                vehicles_file.close()
                print('\n\n')
                prompt = False


class ProcessRequest(six.with_metaclass(BaseClass)):

    def __init__(self, vehicle, country):
        self.vehicle = vehicle
        self.country = country

    def generate_price(self):
        vehicle = list(self.vehicle)
        no_of_letters = len(vehicle)
        return no_of_letters * self.constant_price

    def purchase_vehicle(self):
        purchase_msg = "\n\nThe vehicle you requested %s is accounted  %s\n\n" % (self.vehicle, self.generate_price())
        l1 = len(list(purchase_msg))
        print('-' * l1)
        print(purchase_msg)
        print('-' * l1)
        sys.exit(0)


class UserInterface(Country, Vehicle):

    def auto_check(self):
        missig_vehicles = False
        missing_countries = False
        vehicles = [v for v in self.existingVehicles()]
        if len(vehicles) == 0:
            print("**No vehicles in list, you must add them first\n")
            missig_vehicles = True

        countries = [v for v in self.existingCountries()]
        if len(countries) == 0:
            print("**No Countries in list, you must add them first\n")
            missing_countries = True

        return missig_vehicles, missing_countries

    def options(self):
        opt = OrderedDict((
            ('1', ('Add Countries', self.addCountry)),
            ('2', ('View Countries', self.show_countries)),
            ('3', ('Add Vehicles', self.addVehicle)),
            ('4', ('View Vehicles', self.show_vehicles)),
            ('5', ('Purchase Vehicle', self.purchase))
        ))

        return opt

    def match_choice(self, choice):
        if choice == '5':
            if True in self.auto_check():
                print("You cannot proceed, ensure you add missing values.")
                sys.exit(1)
        options = self.options()
        if choice in options:
            opt = options[choice]
            fn = opt[1]
            return True, fn

        else:
            return False, None

    def select_vehicle(self):
        help_message = "Enter the vehicle name as per the list: "
        print('-' * (len(list(self.banner)) + 10))
        for vehicle in self.existingVehicles():
            print(vehicle.split('\n')[0].strip().capitalize())

        print('-' * (len(list(self.banner)) + 10))
        existing = [vehicle.split('\n')[0] for vehicle in self.existingVehicles()]

        user_choice = raw_input(help_message).lower()
        print("\n")
        if user_choice not in existing:
            print("Oops vehicle not in the list, try again!!\n\n")
            self.select_vehicle()

        else:
            return user_choice

    def select_country(self):
        help_message = "Enter the country name as per the list: "
        print('-' * (len(list(self.banner)) + 10))
        for country in self.existingCountries():
            print(country.split('\n')[0].strip().capitalize())

        print('-' * (len(list(self.banner)) + 10))
        existing = [country.split('\n')[0] for country in self.existingCountries()]

        user_choice = raw_input(help_message).lower()
        print("\n\n")
        if user_choice not in existing:
            print("\nOops country not in the list, try again!!\n\n")
            self.select_country()

        else:
            return user_choice

    def purchase(self):
        vehicle, country = self.select_vehicle(), self.select_country()
        instance = ProcessRequest(vehicle, country)
        return instance.purchase_vehicle()

    def menu(self):
        self.auto_check()
        menu_prompt_msg = "Please enter the number corresponding to the options below\n"
        menu_message = "%s: %s"
        input_message = ""
        help_message = "\nYou can always quit by pressing the keys listed below" \
                       "\n%(exit_keys)s\n" \
                       "but to close the program completely press CTRL + C\n" % dict(
            exit_keys=self.exit_keys)
        print(self.header)
        print(help_message)
        print(menu_prompt_msg)
        for k, v in self.options().items():
            print(menu_message % (k, v[0]))

        print(input_message)
        promt_menu = True
        while promt_menu is True:
            user_choice = raw_input("select your choice: ")
            print("\n")
            if user_choice not in self.exit_keys:
                status = self.match_choice(user_choice)
                if status[0]:
                    option = status[1]
                    option()
                    promt_menu = False

                else:
                    print("You entered an invalid choice, Try again!\n\n")

            else:
                promt_menu = False
                print('\n\n')

        self.menu()


ui = UserInterface()
