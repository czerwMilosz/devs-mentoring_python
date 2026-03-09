def get_user_number() -> int:
    while True:
        try:
            user_number = int(input("Enter positive integer number: "))
            if user_number <= 0:
                print("Please enter a positive integer number")
            else:
                return user_number
        except ValueError:
            print("Please enter an integer number")

def calculate_sum(number:int) -> int:
    num = 0
    total = 0
    while num <= number:
        total += num
        num += 1
    return total

def main():
    user_number = get_user_number()
    total = calculate_sum(user_number)
    print(f"The sum is: {total}")

if __name__ == "__main__":
    main()

