def get_input():
    numbers = []
    while len(numbers) < 3:
        try:
            user_input = float(input('Wprowadz dowolna liczbe: '))
        except ValueError:
            print('To nie jest liczba')
            continue
        numbers.append(user_input)
    return numbers

'''def get_max_value(numbers): #to tylko zeby pokazac jak to szybciej mozna zrobic
    return max(numbers)'''

def get_max_value(numbers: list):
    num1, num2, num3 = numbers
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3

def main():
    numbers = get_input()
    print(get_max_value(numbers))

main()