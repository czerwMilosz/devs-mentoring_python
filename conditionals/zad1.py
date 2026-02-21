def get_intput():
    print("Podaj dlugosci bokow trojkata")
    side_a = float(input("Podaj dlugosc boku a: "))
    side_b = float(input("Podaj dlugosc boku b: "))
    side_c = float(input("Podaj dlugosc boku c: "))
    return (side_a, side_b, side_c)

def sort_tuple_desc(sides: tuple): #sortuje tuple desc
    sorted_tuple = tuple(sorted(sides, reverse=True))
    return sorted_tuple

def pythagorean_check(sides: tuple): #sprawdza czy trojkat spelnia zalozenia
    sorted_sides = sort_tuple_desc(sides)
    if sorted_sides[1] ** 2 + sorted_sides[2] **2  == sorted_sides[0] ** 2:
        return True
    else:
        return False

def main():
    sides = get_intput()
    if pythagorean_check(sides):
        return f'Trójkąt jest prostokątny'
    else:
        return f'Trójkąt nie jest prostokątny'

print(main())