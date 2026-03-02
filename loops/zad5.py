def get_divisor():
    while True:
        try:
            divisor = int(input("Podaj dzielnik: "))
            if divisor != 0:
                return divisor
            else:
                print("Dzielnik nie moze byc rowny 0")
        except ValueError:
            print('Podaj poprawna wartosc')

def get_range():
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

def get_divisible_numbers(user_range, divisor):
    divisible_numbers = []
    if user_range["start"] < user_range["end"]:
        for number in range(user_range["start"], user_range["end"] + 1):
            if number % divisor == 0:
                divisible_numbers.append(number)
    else:
        for number in range(user_range["start"], user_range["end"] -1, -1):
            if number % divisor == 0:
                divisible_numbers.append(number)
    return divisible_numbers

def main():
    user_range = get_range()
    divisor = get_divisor()
    divisible_numbers = get_divisible_numbers(user_range, divisor)
    if len(divisible_numbers) != 0:
        print(f"Liczby z zakresu {user_range['start']}:{user_range['end']} podzielne przez {divisor}: {divisible_numbers}")
    else:
        print(f"Zadna z liczb z zakresu {user_range['start']}:{user_range['end']} nie jest podzielna przez {divisor}")

if __name__ == '__main__':
    main()
