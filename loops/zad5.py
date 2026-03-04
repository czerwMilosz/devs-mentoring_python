def get_divisor() -> int:
    """
        Prompt the user to enter a numeric range.

        The function asks for start and end values and ensures
        they are not equal.

        Returns:
            dict: A dictionary with keys 'start' and 'end'.
        """
    while True:
        try:
            divisor = int(input("Podaj dzielnik: "))
            if divisor != 0:
                return divisor
            else:
                print("Dzielnik nie moze byc rowny 0")
        except ValueError:
            print('Podaj poprawna wartosc')

def get_range() -> dict:
    """
       Prompt the user to enter a non-zero integer divisor.

       Repeats the input request until a valid non-zero integer is provided.

       Returns:
           int: A non-zero integer entered by the user.
       """
    user_range = {}
    while len(user_range) < 2:
        try:
            start = int(input("Podaj pierwsza wartosc przedzialu: "))
            end = int(input("Podaj druga wartosc przedzialu: "))
            if start == end:
                print("\nGorny zakres nie moze byc rowny dolnemu. Podaj ponownie wartosci")
                continue
            else:
                user_range["start"] = start
                user_range["end"] = end
                return user_range
        except ValueError:
            print('Wprowadz poprawna wartosc')

def get_divisible_numbers(user_range:dict, divisor:int) -> list:
    """
        Prompt the user to enter a numeric range.

        The function asks for start and end values and ensures
        they are not equal.

        Returns:
            dict: A dictionary with keys 'start' and 'end'.
        """
    selected_range = (
        range(user_range["start"], user_range["end"] + 1)
        if user_range["start"] < user_range["end"] else
        range(user_range["start"], user_range["end"] - 1, -1)
    )
    divisible_numbers = [number for number in selected_range if number % divisor == 0]

    return divisible_numbers

def main():
    user_range = get_range()
    divisor = get_divisor()
    divisible_numbers = get_divisible_numbers(*[user_range, divisor])
    if len(divisible_numbers) != 0:
        print("Liczby z zakresu {}:{} podzielne przez {}: {}".format(
            user_range['start'],
            user_range['end'],
            divisor,
            divisible_numbers
        ))
    else:
        print(
            f"Zadna z liczb z zakresu {user_range['start']}:"
            f"{user_range['end']} nie jest podzielna przez {divisor}"
        )

if __name__ == '__main__':
    main()


"""print(1,2,3,4)
print(1,2,3,4, sep=", ")
print(1,2,3,4, end="test")
print(1,2,3,4, sep=", ")"""
