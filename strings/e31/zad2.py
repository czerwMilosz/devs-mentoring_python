def kot_ma_ale():
    while True:
        try:
            kotki = int(input('Ile kotow ma Ala? '))
            if kotki > 0:
                break #przerywa petle przy poprawnym typie zmiennej (int)
            else:
                print('Kotki to pozytywne zwierzatka, podaj wartosc powyzej 0')
        except ValueError:
            print('Nie utrudniaj mi zycia, podaj poprawna liczbe..') #nie dopuszcza innych typow oprocz int

    wiecej_magicznych_kotkow = kotki + 3
    magiczne_kotki = f'Teraz Ala ma juz {wiecej_magicznych_kotkow} kotow'.strip()
    podzielone_kotki = magiczne_kotki.replace(' ', ', ')
    drabinka_kotkow = magiczne_kotki.replace(' ', '\n')

    print('Dzisiaj Ala znalazla jeszcze 3 koty w krainie czarow')
    print(magiczne_kotki)
    print(podzielone_kotki)
    print(drabinka_kotkow)

    if not magiczne_kotki.islower():
        print('Kotki sa za duze.. trzeba je zmniejszyc')
        male_magiczne_kotki = magiczne_kotki.lower()
        print(male_magiczne_kotki)
    else:
        print('Nic nie trzeba zmieniac, kotki sa male')

    wiekszy_kotek = male_magiczne_kotki.capitalize()
    print(f'Powiekszamy kotka: {wiekszy_kotek}')
    return 'Piekny byl to program, nie zapomne go nigdy (/^-^)o日日o(^0^|)'

print(kot_ma_ale())