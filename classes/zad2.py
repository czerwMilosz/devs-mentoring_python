class Car:
    def __init__(self, max_speed: float, mileage:float = 0):
        if max_speed <= 0 or mileage < 0:
            raise ValueError("Max speed and mileage cannot be negative")
        self.max_speed = max_speed
        self.mileage = mileage

    def add_mileage(self, mileage:float):
        if mileage < 0:
            raise ValueError("Mileage cannot be negative")

        self.mileage += mileage


def main():
    car = Car(max_speed=180)
    car.add_mileage(mileage=15000)
    car.add_mileage(mileage=500)
    print(car.mileage)

if __name__ == "__main__":
    main()