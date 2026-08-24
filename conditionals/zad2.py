def get_input():
    while True:
        try:
            user_input = float(input('Wprowadz dowolna liczbe: '))
        except ValueError:
            print('To nie jest liczba')
            continue
        return user_input

def classify_number(number):
    if number < 0:
        return f'Wartosc ujemna'
    elif number > 0:
        return f'Wartosc dodatnia'
    else:
        return f'Wartosc rowna 0'


def main():
    number = get_input()
    print(classify_number(number))

main()