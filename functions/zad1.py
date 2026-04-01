NUMS = [4, 6, 8, 24, 12, 2]

def get_biggest_number(numbers: list):
    indexed_numbers = [(index, number) for index, number in enumerate(numbers)]
    return max(indexed_numbers, key=lambda x: x[1])[0]

def get_biggest_number_v2(numbers: list):
    return max(enumerate(numbers), key=lambda x: x[1])[0]


def main():
    index_of_biggest_number = get_biggest_number(NUMS)
    print(get_biggest_number_v2(NUMS))
    print(f"Index of the biggest number is: {index_of_biggest_number}")

if __name__ == '__main__':
    main()