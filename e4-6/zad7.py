def get_user_number() -> float:
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Please enter a number")

def calculate_abs(number: float) -> float:
    return abs(number)

def main():
    number = get_user_number()
    abs_number = calculate_abs(number)
    print("The absolute value of {} is {}".format(number, abs_number))

if __name__ == "__main__":
    main()