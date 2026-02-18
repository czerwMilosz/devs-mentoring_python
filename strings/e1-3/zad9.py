def change_string(word: str):
    if word[-1] in '!?.': #sprawdza czy ostatni element stringa konczy sie zaakiem int.
        new_word = word[-2] + word[1:-2] + word[0] + word[-1]
    elif word[-1] == " ": #sprawdza czy ostatni element jest pustym znakiem
        new_word = word[-2] + word[1:-2] + word[0]
    else:
        new_word = word[-1] + word[1:-2] + word[0]
    return new_word

user_word = str(input('Wprowadz tekst: '))
print(change_string(user_word))