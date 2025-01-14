class Person:
    def __init__(self, email_address: str):
        self._email_address = email_address

    @property
    def email_address(self):
        return self._email_address


class Driver(Person):
    def __init__(self, email_address: str):
        super().__init__(email_address)
        self._vehicle = None

    def take_a_vehicle(self, vehicle):
        if self._vehicle is not None:
            raise VehicleAlreadyAssignedException(
                "Driver already has a vehicle assigned.")
        self._vehicle = vehicle


class Vehicle:
    def __init__(self, chassis_number: str):
        self._chassis_number = chassis_number

    @property
    def chassis_number(self):
        return self._chassis_number


class VehicleAlreadyAssignedException(Exception):
    pass


class VehicleNotFoundException(Exception):
    pass


class DriverNotFoundException(Exception):
    pass


class Enterprise:
    def __init__(self):
        self._drivers = {}
        self._vehicles = {}

    def assign_vehicle_to_driver(self, chassis_number: str, driver_email_address: str):
        driver = self.get_driver_by_email_address(driver_email_address)
        vehicle = self.get_vehicle_by_chassis_number(chassis_number)
        driver.take_a_vehicle(vehicle)

    def get_driver_by_email_address(self, email_address: str):
        if email_address not in self._drivers:
            raise DriverNotFoundException(
                f"Driver with email {email_address} not found.")
        return self._drivers[email_address]

    def get_vehicle_by_chassis_number(self, chassis_number: str):
        if chassis_number not in self._vehicles:
            raise VehicleNotFoundException(f"Vehicle with chassis number {
                                           chassis_number} not found.")
        return self._vehicles[chassis_number]

    def add_driver(self, driver: Driver):
        self._drivers[driver.email_address] = driver

    def add_vehicle(self, vehicle: Vehicle):
        self._vehicles[vehicle.chassis_number] = vehicle
