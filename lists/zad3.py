LIST1 = ["abc", "def", "ghi", "jkl"]
LIST2 = [1, 2, 3, 4, 5]
LIST3 = ["xyz", 1, '2']

def create_dict_from_lists(list1, list2, list3) -> dict:
    return {
        "list1": list1,
        "list2": list2,
        "list3": list3
    }

def pkt_c(list2, list3):
    list2[1] = list3[1]
    return list2

def pkt_d(list3, user_input):
    list3[2] = user_input
    return list3

def pkt_e(list1, word="slowo"):
    list1.append(word)
    return list1

def pkt_f(list1, index = 2):
    del list1[index]
    return list1

def pkt_h(list1, list3):
    list1.extend(list3)
    return list1


def main():
    lists = create_dict_from_lists(LIST1, LIST2, LIST3)
    user_input = input("Enter a text ")
    for key, value in lists.items():
        print(f"{key}: {value}")

    print(f"First element of list1: {LIST1[0]} and fourth element: {LIST1[3]}")
    print(f"List 2 with value from List3: {pkt_c(LIST2, LIST3)}")
    print(f"List 3 with value from user input : {pkt_d(LIST3, user_input)}")
    print(f"List 1 with new word: {pkt_e(LIST1)}")
    print(f"List 1 with deleted element on index 2 {pkt_f(LIST1)} ")
    print(f"Length of list 3: {len(LIST3)}")
    print(f"List1 extended by list 3: {pkt_h(LIST1, LIST3)}")




if __name__ == "__main__":
    main()
