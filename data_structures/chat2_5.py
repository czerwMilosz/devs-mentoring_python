# 5. Grupowanie ludzi po mieście

from collections import defaultdict

PEOPLE = [
    ("Anna", "Warsaw"),
    ("Jan", "Krakow"),
    ("Ola", "Warsaw"),
    ("Piotr", "Gdansk"),
    ("Kasia", "Krakow")
]

def group_by_city(people: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped_people = defaultdict(list)
    for person, city in people:
        grouped_people[city].append(person)
    return dict(grouped_people)

def main():
    print(group_by_city(PEOPLE))

if __name__ == '__main__':
    main()