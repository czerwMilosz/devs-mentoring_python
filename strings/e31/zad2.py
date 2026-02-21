def weryfikacja_kotkow():
    while True:
        try:
            ilosc_kotkow = int(input('Ile kotow ma Ala? '))
            if ilosc_kotkow > 0:
                break  # przerywa petle gdy uzytkownik podal wartosc > 0
            else:
                print('Ala zawsze ma jakies kotki, podaj wartosc powyzej 0')
        except ValueError:
            print('Nie utrudniaj mi zycia, podaj poprawna ilosc..')  # Nie przerywa programu z bledem, tylko wyswietla komunikat, przez co petla caly czas dziala i ponownie mozna wpisac wartosc
    return ilosc_kotkow

def male_kotki(kotki: str):
    if not kotki.islower():
        return kotki.lower()
    else:
        return kotki

def kot_ma_ale():
    kotki_ali = weryfikacja_kotkow()
    wiecej_magicznych_kotkow = 'Dzisiaj Ala znalazla jeszcze 3 koty w krainie czarow'
    ilosc_magicznych_kotkow = kotki_ali + 3
    magiczne_kotki = f'Teraz Ala ma juz {ilosc_magicznych_kotkow} kotow'
    podzielone_kotki = ', '.join(magiczne_kotki.split()) #split dzieli na liste, join laczy elementy listy
    drabinka_kotkow = magiczne_kotki.replace(' ', '\n') #tez mozna uzyc split ale chcialem pokazac druga opcje
    male_magiczne_kotki = male_kotki(magiczne_kotki)
    wiekszy_kotek = male_magiczne_kotki.capitalize()

    print (f'''{wiecej_magicznych_kotkow}
{magiczne_kotki}
{podzielone_kotki}
{drabinka_kotkow}
{male_magiczne_kotki}
{wiekszy_kotek}''')

kot_ma_ale()