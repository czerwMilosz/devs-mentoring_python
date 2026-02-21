def pij_mleko():
    while True:
        text = input("Podaj tekst do powiekszenia: ")
        if text == '':
            print('Tekst nie moze byc pusty!')
        else:
            return text


def bedziesz_wielki():
    user_input = pij_mleko().lower()
    check_string = ''

    for l in user_input: #sprawdza czy tekst zawiera litery do powiekszenia
        if l.isalpha():  #na poczatku chcialem tu uzyc zakresu  i kodow ASCII z ord() ale to nie wykrywalo polskich znakow
            break
        else:
            check_string += l

    if user_input == check_string:
        return f'Tekst nie zawiera liter, to czego sie innego sie spodziewales: {user_input}'
    else:
        return f'Twoj powiekszony tekst: {user_input.upper()}'

print(bedziesz_wielki())
