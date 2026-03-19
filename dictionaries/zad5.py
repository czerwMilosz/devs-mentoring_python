def get_user_number() ->int:
    while True:
        try:
            user_number = int(input("Enter a positive integer: "))
            if user_number <= 0:
                raise ValueError
            return user_number
        except ValueError:
            print("Please enter a valid positive integer")

def generate_square_mapping(number) -> dict:
    return {n: n*n for n in range(1,number+1)}


def main():
    number = get_user_number()
    print(generate_square_mapping(number))

if __name__ == "__main__":
    main()
