
def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

def main():
    print(multiply(2, 3, 5, 7))
    print(multiply(4, 4, 2, 8))
    print(multiply(0, 1, 6, 7))

if __name__ == "__main__":
    main()