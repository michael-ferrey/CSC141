class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 240
        elif self.battery_size == 100:
            range = 315
        return range

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already at maximum capacity.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def get_range(self):
        return self.battery.get_range()


if __name__ == "__main__":
    my_electric_car = ElectricCar("Tesla", "Model S", 2022)
    print(f"Range with default battery: {my_electric_car.get_range()} miles")

    my_electric_car.battery.upgrade_battery()

    print(f"Range after battery upgrade: {my_electric_car.get_range()} miles")
