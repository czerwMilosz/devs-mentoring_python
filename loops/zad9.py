def get_fuel_level() -> float:
    """
       Prompt the user to enter the initial fuel level.

       The function validates that the fuel level is a numeric value
       between 5000 and 30000 liters.

       Returns:
           float: A valid fuel level in liters.
       """
    while True:
        try:
            fuel_level = float(input("Enter fuel level: "))
            if 5000 <= fuel_level <= 30000:
                return fuel_level
            else:
                print("Sorry, fuel level must be between 5000 and 30000")
        except ValueError:
            print("Please enter a numeric value.")

def get_astronaut_amount() -> int:
    """
       Prompt the user to enter the initial fuel level.

       The function validates that the fuel level is a numeric value
       between 5000 and 30000 liters.

       Returns:
           float: A valid fuel level in liters.
       """
    while True:
        try:
            astronaut_amount = int(input("Enter astronaut amount: "))
            if astronaut_amount > 7:
                print("Sorry, astronaut amount must be between 1 and 7")
            elif astronaut_amount < 1:
                print("Sorry, astronaut amount cannot be less than 1")
            else:
                return astronaut_amount
        except ValueError:
            print("Please enter an integer value.")


def calculate_distance(fuel_level: float, astronaut_amount: int) -> int:
    """
    Simulate the flight of a spaceship and calculate the traveled distance.

    Fuel consumption per 100 km is calculated as:
        300 + 100 * astronaut_amount

    Args:
        fuel_level (float): Initial fuel level in liters.
        astronaut_amount (int): Number of astronauts on board.

    Returns:
        int: Total distance traveled in kilometers.
    """
    distance = 0
    fuel_usage = 300 + 100 * astronaut_amount
    while fuel_level >= fuel_usage:
        fuel_level -= fuel_usage
        distance += 100
        print(f"Reached distance: {distance} km")
    return distance

def check_flight_status(distance: int) -> bool:
    """
        Check whether the spaceship reached orbit.

        Args:
            distance (int): Total distance traveled in kilometers.

        Returns:
            bool: True if the spaceship reached orbit (distance > 2000),
                  otherwise False.
        """
    return distance > 2000

def main():
    fuel_level = get_fuel_level()
    astronaut_amount = get_astronaut_amount()
    distance = calculate_distance(fuel_level, astronaut_amount)
    if check_flight_status(distance):
        print("The spaceship reached orbit.")
    else:
        print("The spaceship did not reach orbit.")

if __name__ == "__main__":
    main()