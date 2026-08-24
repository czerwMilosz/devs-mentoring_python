list_a = [1,2,3,4,5,6]
list_b = [4,5,6,7,8,9]

def has_common_element(list1, list2):
   return bool(set(list1) & set(list2))

def main():
    if has_common_element(list_a, list_b):
        print("Lists have at least one common element")
    else:
        print("Lists do not have any common elements")

if __name__ == "__main__":
    main()