def get_user_integer() -> int:
    while True:
        try:
            user_number = int(input("Please enter an integer number: "))
            return user_number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_divisors(number:int) -> list:
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
    return divisors


def is_perfect_number(divisors: list, number: int) -> bool:
    return sum(divisors) == number

def main():
    user_number = get_user_integer()
    divisors = get_divisors(user_number)
    if is_perfect_number(divisors, user_number):
        print(f"{user_number} is the perfect number.")
    else:
        print(f"{user_number} is not the perfect number.")

if __name__ == "__main__":
    main()


