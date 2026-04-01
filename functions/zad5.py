
def zip_numbers(**kwargs):
    even = kwargs.get("even", [])
    odd = kwargs.get("odd", [])
    new_list = []
    for pair in zip(odd, even):
        for num in pair:
            new_list.append(num)
    return new_list


def main():
    even = [2,4,6,8]
    odd = [3,5,7,9]
    print(zip_numbers(even=even, odd=odd))

if __name__ == "__main__":
    main()