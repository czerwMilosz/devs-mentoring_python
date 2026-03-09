D = (1, [2, 4], 'tekst', 3 + 5j)

def get_last_element(d: tuple):
    return d[-1]

def get_first_two_elements(d: tuple):
    return [d[0], d[1]]

def check_if_in_tuple(d: tuple):
    return "abc" in d

def main():
    last_element = get_last_element(D)
    first_two_elements = get_first_two_elements(D)
    check_if_in_tuple(first_two_elements)
    print(f"Tuple: {D}"
          f"\nLast element: {last_element}"
          f"\nFirst two elements: {first_two_elements}"
          f"\nCheck if abc is in tuple: {check_if_in_tuple(D)}")

if __name__ == "__main__":
    main()