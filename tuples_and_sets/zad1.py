COLORS = [
    'zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy',
    'granatowy', 'niebieski', 'czarny', 'czarny', 'zielony',
    'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony'
]

def convert_list_to_set(lst: list) -> set:
    return set(lst)

colors_set = convert_list_to_set(COLORS)

def get_len_of_set(lst: list) -> int:
    return len(lst)

def print_set(colors_set: set):
    for color in colors_set:
        print(color)

def add_colors_to_set(colors_set: set):
    color = input('Enter a color: ')
    colors_set.add(color)
    return colors_set

def delete_colors_from_set(colors_set: set):
    color = input('Enter a color: ')
    colors_set.discard(color)
    return colors_set

