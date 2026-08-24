def get_user_number():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Please enter a number")

def fizz_buzz(number: int) -> str | int:

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

def fizz_buzz_v2(number: int) -> str | int:
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    return result or number

def main():
    number = get_user_number()
    print(fizz_buzz(number))
    print(fizz_buzz_v2(number))

if __name__ == "__main__":
    main()