from random import randint

def input_min_length(length = 7):
    text = input("Wprowadz tekst (min 7 znakow): ").strip()
    while len(text) < length:
        text = input("Wprowadz tekst (min 7 znakow): ")
    return text

def string_properties(text = input_min_length()):
    string_length = len(text)
    first_char = text[0]
    last_char = text[-1]
    rand_first_num = randint(1, string_length // 2)
    random_middle_text = text[rand_first_num:rand_first_num + 3]
    return f'''Twoj tekst: {text}
Dlugosc tekstu: {string_length}
Pierwsza litera: {first_char}
Ostatnia litera: {last_char}
Losowe 3 znaki ze srodka tesktu: {random_middle_text}
'''

print(string_properties())


