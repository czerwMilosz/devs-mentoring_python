def reverse_kwargs(**kwargs):
    result = {}

    for key, value in kwargs.items():
        result[value] = key

    return result


def main():
    print(reverse_kwargs(a=1, b=2, c=3))
    print(reverse_kwargs(name="Adam", city="Berlin"))


if __name__ == "__main__":
    main()