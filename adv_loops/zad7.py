def get_user_number():
    while True:
        try:
            number = int(input("Enter an integer: "))
            if number < 0:
                raise ValueError
            return number
        except ValueError:
            print("Please enter a non-negative integer")

def fibonacci(number:int):
    a, b = 0, 1
    for _ in range(number):
        a, b = b, a + b
    return a

def main():
    number = get_user_number()
    print(f"Fibonacci number for {number}: {fibonacci(number)}")

if __name__ == "__main__":
    main()
