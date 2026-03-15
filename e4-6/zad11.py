def zad11_a(width = 7, height = 6):
    for i in range(height):
        print("*" * width)

# print(zad11_a())

def zad11_b(width = 5, height = 5):
    for i in range(height):
        if i == 0 or i == height-1:
            print("*" * width)
        else:
            print("*" + " " * (width - 2) + "*")

#print(zad11_b())

def zad11_c(height = 5):
    for i in range(height):
        # spacje
        for j in range(height - i - 1):
            print(" ", end="")

        # gwiazdy
        for j in range(2 * i + 1):
            print("*", end="")

        print()


print(zad11_c())

    