from math import ceil

def print_shape(height:int = 10):
    half_height_ceil = ceil(height/2)
    for h in range(1, half_height_ceil + 1):
        print("* " * (h-1) + "*")
    for h in range(half_height_ceil - 1, 0, -1):
        print("* " * (h-1) + "*")


def main():
    print_shape()

if __name__ == "__main__":
    main()
