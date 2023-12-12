class Car:
    def __init__(self, make, model, fuel_level=100):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level
        self.is_running = False

    def start(self):
        if self.fuel_level > 0:
            print(f"{self.make} {self.model} started. Ready to go!")
            self.is_running = True
        else:
            print("No fuel. Cannot start the car.")

    def stop(self):
        if self.is_running:
            print(f"{self.make} {self.model} stopped.")
            self.is_running = False
        else:
            print(f"{self.make} {self.model} is not running.")

    def check_fuel_level(self):
        print(f"Fuel level in {self.make} {self.model}: {self.fuel_level}%")

# Instantiate the Car class
my_car = Car(make="Toyota", model="Camry")

# Call methods to illustrate functionality
my_car.start()
my_car.check_fuel_level()

# Simulate driving (depleting fuel)
for _ in range(3):
    my_car.start()
    my_car.stop()

my_car.check_fuel_level()
