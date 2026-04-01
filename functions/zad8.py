def get_clock(hour, minute):
    return abs(30*hour - 5.5 * minute)


def main():
    hour = 0
    minute = 0
    print(get_clock(hour, minute))

if __name__ == "__main__":
    main()