
def zip_numbers(**kwargs):
    even = kwargs.get("even", [])
    odd = kwargs.get("odd", [])
    new_list = []
    for pair in zip(odd, even):
        for num in pair:
            new_list.append(num)
    return new_list


def zip_numbers_2(*iterables):
    new_list = []
    min_len = min(len(iterable) for iterable in iterables)
    for i in range(min_len):
        new_list.extend(tuple(iterable[i] for iterable in iterables))
    return new_list

from itertools import chain

def zip_numbers_3(*iterables):
    min_len = min(len(iterable) for iterable in iterables)
    for i in range(min_len):
        yield tuple(iterable[i] for iterable in iterables)


def main():
    even = [2,4,6,8,10]
    odd = [3,5,7,9,11]
    print(zip_numbers(even=even, odd=odd))
    print(zip_numbers_2(even, odd))
    print(list(chain.from_iterable(zip_numbers_3(even, odd))))

if __name__ == "__main__":
    main()