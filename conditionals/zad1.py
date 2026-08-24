def get_input():
    print("Podaj dlugosci bokow trojkata")
    side_a = float(input("Podaj dlugosc boku a: "))
    side_b = float(input("Podaj dlugosc boku b: "))
    side_c = float(input("Podaj dlugosc boku c: "))
    return (side_a, side_b, side_c)

def pythagorean_check(sides: tuple): #sprawdza czy trojkat spelnia zalozenia
    sorted_sides = sorted(sides, reverse=True)
    if sorted_sides[1] **2 + sorted_sides[2] **2  == sorted_sides[0] **2:
        return True
    else:
        return False

def main():
    sides = get_input()
    if pythagorean_check(sides):
        print('Trojkat jest prostokatny')
    else:
        print('Trojkat nie jest prostokatny')

main()