def get_number():
    while True:
        try:
            number = int(input("Wprowdz liczbe calkowita: "))
            return number
        except ValueError:
            print('Podaj poprawna wartosc')


def get_total():
    total = 0
    previous_total = 0
    while True:
        number = get_number()
        total += number
        print(f"Aktualna suma: {total}")
        if total <= previous_total:
            break
        previous_total = total
    return total

def main():
    result = get_total()
    print(f"Finalny wynik: {result}")

if __name__ == '__main__':
    main()
