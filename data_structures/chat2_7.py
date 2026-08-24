# 7. Odwrócony słownik
from collections import defaultdict

grades = {
    "Anna": "A",
    "Jan": "B",
    "Ola": "A",
    "Piotr": "C",
    "Kasia": "B"
}

def invert_grades(grades: dict[str, str]) -> dict[str, list[str]]:
    d = defaultdict(list)
    for person, grade in grades.items():
        d[grade].append(person)
    return dict(d)

def main():
    print(invert_grades(grades))

if __name__ == '__main__':
    main()