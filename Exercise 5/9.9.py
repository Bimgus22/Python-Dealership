class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range_miles = 240
        elif self.battery_size == 85:
            range_miles = 300

        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("Tesla", "Model S", 2024)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
