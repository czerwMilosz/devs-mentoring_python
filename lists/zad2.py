from random import randint
RESULT = [12,1,45,76,50,23]

def replace_invalid_numbers(numbers: list, max_value:int = 49) -> list:
    return [randint(1, max_value) if number < 1 or number > max_value
            else number for number in numbers] # for fun

def replace_invalid_numbers_v2(numbers: list, max_value:int = 49) -> list:
    new_list = []
    for number in numbers:
        if number < 1 or number > max_value:
            new_number = randint(1, max_value)
            new_list.append(new_number)
            print(f"{number} is invalid -> replaced with {new_number}")
        else:
            new_list.append(number)
    return new_list

def main():
    print(replace_invalid_numbers(RESULT))
    print(replace_invalid_numbers_v2(RESULT))

if __name__ == "__main__":
    main()