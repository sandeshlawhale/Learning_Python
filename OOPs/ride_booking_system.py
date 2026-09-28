class Driver:
    def __init__(self, name, d_id, vehicle):
        self.name = name
        self.d_id = d_id
        self.vehicle = vehicle
        self.status = "AVAILABLE"

    def start_ride(self):
        self.status = "BUSY"

    def complete_ride(self):
        self.status = "AVAILABLE"


class Vehicle:
    def __init__(self, reg_num, base_fare):
        self.reg_num = reg_num
        self.base_fare = base_fare


class Car(Vehicle):
    def calculate_fare(self, distance):
        return self.base_fare + distance * 15


class Auto(Vehicle):
    def calculate_fare(self, distance):
        return self.base_fare + distance * 10


class Bike(Vehicle):
    def calculate_fare(self, distance):
        return self.base_fare + distance * 7


class Ride:
    def __init__(self, customer_name, driver, distance):
        if driver.status == "BUSY":
            # warn that you cannot book the driver
            raise ValueError("Driver is currently busy")

        self.customer_name = customer_name
        self.driver = driver
        self.distance = distance
        self.fare = driver.vehicle.calculate_fare(distance)

        driver.start_ride()


# Create vehicles
car = Car("TS09AB1234", 50)
bike = Bike("TS09CD5678", 30)
auto = Auto("TS09EF9012", 40)


# Create drivers
rahul = Driver("Rahul", "D101", car)
amit = Driver("Amit", "D102", bike)
suresh = Driver("Suresh", "D103", auto)


# Check initial status
print("rahul.status", rahul.status)
print("amit.status", amit.status)
print("suresh.status", suresh.status)


# Create a ride
ride1 = Ride("Jane", rahul, 10)

print("\nRide 1")
print("Customer:", ride1.customer_name)
print("Driver:", ride1.driver.name)
print("Distance:", ride1.distance)
print("Fare:", ride1.fare)
print("Driver status:", rahul.status)


# Try booking the same driver again
print("\nTrying to book Rahul again...")

try:
    ride2 = Ride("John", rahul, 5)
except ValueError as e:
    print("Error:", e)
