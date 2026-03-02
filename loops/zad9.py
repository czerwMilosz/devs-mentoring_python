def get_fuel_level() -> float:
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


def calculate_distance(fuel_level: float, astronaut_amount: int):
    distance = 0
    fuel_usage = 300 + 100 * astronaut_amount
    while fuel_level >= fuel_usage:
        fuel_level -= fuel_usage
        distance += 100
        print(f"Reached distance: {distance} km")
    return distance

def check_flight_status(distance: int):
    if distance > 2000:
        print("The spaceship reached orbit.")
    else:
        print("The spaceship did not reach orbit.")

def main():
    fuel_level = get_fuel_level()
    astronaut_amount = get_astronaut_amount()
    distance = calculate_distance(fuel_level, astronaut_amount)
    check_flight_status(distance)

if __name__ == "__main__":
    main()