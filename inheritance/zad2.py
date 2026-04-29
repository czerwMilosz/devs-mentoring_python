"""
Module defining a simple object-oriented model of public transport vehicles
(buses and trams) and their depots, including basic validation, relationships,
and string representations.
"""

class Vehicle:
    """Base class representing a generic vehicle."""
    def __init__(self, number:int, max_speed:int):
        """Initialize a vehicle with number and maximum speed."""
        if number < 1 or max_speed < 1:
            raise ValueError("Number and max speed must be greater than 0")
        self.number = number
        self.max_speed = max_speed
        self.depot = None

    def __str__(self):
        """Return a human-readable description of the vehicle."""
        if self.depot is None:
            return (f"Number: {self.number}, "
                    f"Max Speed: {self.max_speed}, "
                    f"Depot name: No depot assigned, ")
        else:
            return (f"Number: {self.number}, "
                    f"Max Speed: {self.max_speed}, "
                    f"Depot name: {self.depot.name}, ")

class Depot:
    """Base class representing a depot that stores vehicles."""
    def __init__(self, name:str):
        """Initialize a depot with a name and empty vehicle list."""
        if name.strip() == "":
            raise ValueError("Name cannot be empty")
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle:Vehicle):
        """Add a vehicle to the depot and assign this depot to it."""
        self.vehicles.append(vehicle)
        vehicle.depot = self

    def get_vehicles_description(self):
        """Return a string description of all vehicles in the depot."""
        vehicle_string = []
        for vehicle in self.vehicles:
            vehicle_string.append(str(vehicle))

        vehicle_text = "\n".join(vehicle_string)

        return vehicle_text

    def __str__(self):
        """Return a basic string representation of the depot."""
        return f"Name: {self.name}, "

class BusDepot(Depot):
    """Depot specialized for storing buses and tracking fuel consumption."""
    def __init__(self, name:str):
        """Initialize a bus depot with a name and fixed depot type."""
        super().__init__(name)
        self.depot_type = "Bus Depot"

    def add_vehicle(self, vehicle:Vehicle):
        """Add a bus to the depot with type and uniqueness validation."""
        if not isinstance(vehicle, Bus):
            raise ValueError("Only buses are allowed in bus depot")

        for bus in self.vehicles:
            if bus.number == vehicle.number:
                raise ValueError("Bus with same number already exists")
        super().add_vehicle(vehicle)

    def total_fuel_consumption(self):
        """Calculate total monthly fuel consumption of all buses."""
        total = 0
        for vehicle in self.vehicles:
            total += vehicle.monthly_fuel_consumption
        return total

    def __str__(self):
        """Return a full description of the bus depot and its vehicles."""
        return (super().__str__() +
                f"Depot Type: {self.depot_type}, "
                f"Total Fuel Consumption: {self.total_fuel_consumption()}"
                f"\nAll buses: \n{self.get_vehicles_description()}")

class TramDepot(Depot):
    """Depot specialized for storing trams and tracking wagon counts."""
    def __init__(self, name:str):
        """Initialize a tram depot with a name and fixed depot type."""
        super().__init__(name)
        self.depot_type = "Tram Depot"

    def add_vehicle(self, vehicle:Vehicle):
        """Add a tram to the depot with type and uniqueness validation."""
        if not isinstance(vehicle, Tram):
            raise ValueError("Only trams are allowed in tram depot")

        for tram in self.vehicles:
            if tram.number == vehicle.number:
                raise ValueError("Tram with same number already exists")
        super().add_vehicle(vehicle)

    def total_wagon_count(self):
        """Calculate total number of wagons across all trams."""
        total = 0
        for vehicle in self.vehicles:
            total += vehicle.wagon_count
        return total

    def __str__(self):
        """Return a full description of the tram depot and its vehicles."""
        return (super().__str__() +
                f"Depot Type: {self.depot_type}, "
                f"Total Wagon Count: {self.total_wagon_count()}"
                f"\nAll trams: \n{self.get_vehicles_description()}")


class Bus(Vehicle):
    """Class representing a bus with fuel consumption."""
    def __init__(self,
                 number:int,
                 max_speed:int,
                 monthly_fuel_consumption:float):
        """Initialize a bus with number, speed, and monthly fuel consumption."""
        super().__init__(number, max_speed)

        if monthly_fuel_consumption <= 0:
            raise ValueError("Monthly fuel consumption must be greater than 0")
        self.monthly_fuel_consumption = monthly_fuel_consumption

    def __str__(self):
        """Return a string description of the bus."""
        return (super().__str__() +
                f"Monthly Fuel Consumption: {self.monthly_fuel_consumption}")

class Tram(Vehicle):
    """Class representing a tram with a fixed number of wagons."""
    def __init__(self,
                 number:int,
                 max_speed:int,
                 wagon_count:int):
        """Initialize a tram with number, speed, and wagon count (1–3)."""
        super().__init__(number, max_speed)

        if wagon_count < 1 or wagon_count > 3:
            raise ValueError("Wagon count must be between 1 and 3")
        self.wagon_count = wagon_count

    def __str__(self):
        """Return a string description of the tram."""
        return super().__str__() + f"Wagon Count: {self.wagon_count}"


def main():
    """Create sample depots and vehicles, assign them, and print summaries."""
    bus_depot = BusDepot("Bus paradise")
    bus = Bus(1, 100,  500)
    bus_2 = Bus(2, 200, 400)
    bus_depot.add_vehicle(bus)
    bus_depot.add_vehicle(bus_2)
    print(bus_depot)

    tram_depot = TramDepot("Tram paradise")
    tram = Tram(1, 100, 3)
    tram_2 = Tram(2, 200, 2)
    tram_depot.add_vehicle(tram)
    tram_depot.add_vehicle(tram_2)
    print(tram_depot)


if __name__ == "__main__":
    main()


#todo zapytac o wzorce projektowe chata
#system design software architecture
#dokumentacje, materialy