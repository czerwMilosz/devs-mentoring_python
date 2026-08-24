def get_user_integer() -> int:
    """
    Prompt the user to enter an integer.

    Repeats the request until a valid integer is provided.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            user_number = int(input("Please enter an integer number: "))
            return user_number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_divisors(number:int) -> list:
    """
        Prompt the user to enter an integer.

        Repeats the request until a valid integer is provided.

        Returns:
            int: The integer entered by the user.
    """
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
    return divisors


def is_perfect_number(divisors: list, number: int) -> bool:
    """
    Return a list of proper divisors of the given number.

    Proper divisors are all positive integers less than the number
    that divide it evenly.

    Args:
        number (int): The number to find divisors for.

    Returns:
        list: A list of proper divisors of the number.
    """
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


