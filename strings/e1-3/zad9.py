def change_string(word: str):
    if word.endswith(('!', '?', '.')): #sprawdza czy ostatni element stringa konczy sie zaakiem int.
        new_word = word[-2] + word[1:-2] + word[0] + word[-1]
    elif word.endswith(' '): #sprawdza czy ostatni element jest pustym znakiem
        new_word = word[-2] + word[1:-2] + word[0]
    else:
        new_word = word[-1] + word[1:-2] + word[0]
    word.endswith(' ')
    return new_word

def change_string_v2(word: str):
    clean = word.translate(str.maketrans('', '', '!? .'))
    changed = clean != word
    if len(clean) > 1:
        first, *middle, last = clean
        clean = last + "".join(middle) + first
    return clean + "." * changed



user_word = str(input('Wprowadz tekst: '))
#print(change_string(user_word))
print(change_string_v2(user_word))



# matching pattern poczytac https://peps.python.org/pep-0634/
# https://realpython.com/structural-pattern-matching/