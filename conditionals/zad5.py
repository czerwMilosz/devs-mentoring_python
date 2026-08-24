def get_input():
    numbers = []
    while len(numbers) < 2:
        try:
            user_input = float(input('Wprowadz dowolna liczbe: '))
        except ValueError:
            print('To nie jest liczba')
            continue
        numbers.append(user_input)
    return numbers

def get_even_number(numbers: list):
    if numbers[0] % 2 == 0 and numbers[1] % 2 != 0:
        return f'{numbers[0]} jest liczba parzysta'
    elif numbers[1] % 2 == 0 and numbers[0] % 2 != 0:
        return f'{numbers[1]} jest liczba parzysta'
    elif numbers[0] % 2 == 0 and numbers[1] % 2 == 0:
        return f'{numbers[0]}, {numbers[1]} sa liczbami parzystymi'
    else:
        return f'Podane liczby: {numbers} nie sa parzyste'

def main():
    numbers = get_input()
    print(get_even_number(numbers))

main()