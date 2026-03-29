# 8. Wspólne elementy dwóch list

LIST1 = [1, 2, 3, 4, 5]
LIST2 = [4, 5, 6, 7]

def common_elements(list1: list[int], list2: list[int]) -> set[int]:
    return set(list1) & set(list2)

def main():
    print(common_elements(LIST1, LIST2))

if __name__ == '__main__':
    main()