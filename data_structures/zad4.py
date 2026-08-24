def get_city() -> str:
    """Prompts user for a city name; empty input ends data entry."""
    while True:
        try:
            city = input("Enter a city: ").strip()

            if not city:
                return city

            if not any(char.isalpha() for char in city):
                raise ValueError
            return city
        except ValueError:
            print("Please enter a valid city")

def get_rainfall() -> float:
    """Prompts user for a city name; empty input ends data entry."""
    while True:
        try:
            rainfall = float(input("Enter a rainfall: "))
            return rainfall
        except ValueError:
            print("Please enter a valid rainfall")

def get_total_rainfall() -> dict[str, float]:
    """Prompts user for rainfall amount and returns it as a float."""
    data: dict[str, float] = {}
    while True:
        city = get_city()
        if not city:
            break
        rainfall = get_rainfall()
        data[city] = data.get(city, 0) + rainfall
    return data

def main():
    data = get_total_rainfall()
    for city, rainfall in data.items():
        print(f"{city}: {rainfall}")

if __name__ == "__main__":
    main()

