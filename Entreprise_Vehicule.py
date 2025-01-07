class Person:
    def __init__(self, emailAddress: str):
        self.__emailAddress = emailAddress


class Driver(Person):
    def takeAVehicle(self, vehicle):
        if hasattr(self, '__vehicles'):
            raise VehiculeAlreadyAssignedException(
                "Driver already has a vehicle assigned.")
        self.__vehicle = vehicle


class Vehicle:
    def __init__(self, chassisNumber: str):
        self.__chassisNumber = chassisNumber


class VehiculeAlreadyAssignedException(Exception):
    pass


class VehiculeNotFoundException(Exception):
    pass


class DriverNotFoundException(Exception):
    pass


class Enterprise:
    def __init__(self):
        self.__drivers = {}
        self.__vehicles = {}

    def assignVehicleToDriver(self, chassisNumber: str, driverEmailAddress: str):
        driver = self.getDriverByEmailAddress(driverEmailAddress)
        vehicle = self.getVehicleByChassisNumber(chassisNumber)
        driver.takeAVehicle(vehicle)

    def getDriverByEmailAddress(self, emailAddress: str):
        if emailAddress not in self.__drivers:
            raise DriverNotFoundException(
                f"Driver with email {emailAddress} not found.")
        return self.__drivers[emailAddress]

    def getVehicleByChassisNumber(self, chassisNumber: str):
        if chassisNumber not in self.__vehicles:
            raise VehiculeNotFoundException(f"Vehicle with chassis number {
                                            chassisNumber} not found.")
        return self.__vehicles[chassisNumber]
