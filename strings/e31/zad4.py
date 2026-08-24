def pij_mleko():
    while True:
        text = input("Podaj tekst do powiekszenia: ")
        if text == '':
            print('Tekst nie moze byc pusty!')
        else:
            return text


def bedziesz_wielki(text: str) -> str:
    lower_text = text.lower()
    check_string = ''

    for l in lower_text: # sprawdza czy tekst zawiera litery do powiekszenia
        if l.isalpha():  # na poczatku chcialem tu uzyc zakresu  i kodow ASCII z ord() ale to nie wykrywalo polskich znakow
            break
        else:
            check_string += l

    if lower_text == check_string:
        return f'Tekst nie zawiera liter, to czego sie innego sie spodziewales: {lower_text}'
    return f'Twoj powiekszony tekst: {lower_text.upper()}'

def main():
    user_input = pij_mleko()
    result = bedziesz_wielki(user_input)
    print(result)

if __name__ == '__main__':
    main()