
NESTED = [[1, 2], [3, 4, 5], [], [6]]

def flatten_once(nested: list[list[int]]) -> list[int]:
    new_list = []
    for element in nested:
        new_list.extend(element)
    return new_list

def main():
    print(flatten_once(NESTED))

if __name__ == "__main__":
    main()