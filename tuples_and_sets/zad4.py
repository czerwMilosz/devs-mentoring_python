def get_user_number():
    while True:
        try:
            user_number = int(input('Enter a number: '))
            if user_number < 0:
                raise ValueError
            return user_number
        except ValueError:
            print('Invalid input')

def get_set_numbers(number:int, divisor: int, remainder: int) -> set:
    return {i for i in range(number) if i % divisor == remainder}

def get_set_operations(set_a, set_b):
    set_c = set_a | set_b
    set_d = set_a & set_b
    set_e = set_a - set_b
    set_f = set_a ^ set_b
    return {"set_a": set_a, "set_b": set_b, "set_c": set_c,
            "set_d": set_d, "set_e": set_e, "set_f": set_f}

def main():
    number = get_user_number()
    set_a = get_set_numbers(number, 2, 0)
    set_b = get_set_numbers(number, 3, 2)
    operations = get_set_operations(set_a, set_b)
    for key, value in operations.items():
        print(f"Name: {key}"
              f"\nLength: {len(value)}"
              f"\nValues: {value}")
    print(f"Is set_b subset of set_a: {set_b.issubset(set_a)}")

if __name__ == '__main__':
    main()


