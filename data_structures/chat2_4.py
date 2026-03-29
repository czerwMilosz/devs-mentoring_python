# 4. Usuń duplikaty, ale zachowaj kolejność

numbers = [1, 2, 2, 3, 1, 4, 3, 5]

def unique_in_order(items: list[int]) -> list[int]:
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def unique_in_order_v2(items: list[int]) -> list[int]:
    unique_items = []
    item_set = set()
    for item in items:
        if item not in item_set:
            item_set.add(item)
            unique_items.append(item)
    return unique_items

def main():
    print(unique_in_order(numbers))
    print(unique_in_order_v2(numbers))

if __name__ == '__main__':
    main()