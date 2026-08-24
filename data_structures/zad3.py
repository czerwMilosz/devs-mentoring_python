DICT = {"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}

def invert_dictionary(dictionary:dict[str, int]) -> dict[int, str]:
    """ Returns a new dictionary with keys and values swapped."""
    return {value: key for key, value in dictionary.items()}

def main():
    print(invert_dictionary(DICT))

if __name__ == "__main__":
    main()
