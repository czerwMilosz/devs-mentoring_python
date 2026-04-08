
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

def function_1(a,b,/):
    print(a,b)

def function_2(a, *, b, c):
    print(a,b,c)


def power(base, exponent, /, *, modulo = None, **kwargs):
    result = base ** exponent
    if modulo:
        result %= modulo
    print(kwargs)
    return result

def main():
    print(multiply(2, 3, 5, 7))
    print(multiply(4, 4, 2, 8))
    print(multiply(0, 1, 6, 7))
    function_1(1,2)
    # function_1(a = 3, b = 4)
    function_2(1.5, b = 3, c = 5)
    # function_2(3,4,5)
    print(power(2,3))
    print(power(3,4, modulo = 5))
    print(power(1,2, base = 2, exponent = 5))

if __name__ == "__main__":
    main()