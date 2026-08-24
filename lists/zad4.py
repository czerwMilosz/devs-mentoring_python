def get_user_number() -> int:
    while True:
        try:
            number = int(input("Enter number of friends: "))
            if number < 1:
                raise ValueError
            return number
        except ValueError:
            print("Enter a valid number")

def get_user_names(number:int) -> list:
    names = []
    while len(names) < number:
        try:
            name = input("Enter a name: ")
            if name == "" or name.isalpha() is False:
                raise ValueError
            names.append(name)
        except ValueError:
            print("Enter a valid name")
    return names

def main():
    numbers = get_user_number()
    names = get_user_names(numbers)
    for name in names:
        print(f"Hello {name}!")

if __name__ == "__main__":
    main()

