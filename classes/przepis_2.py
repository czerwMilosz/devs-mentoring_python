class Skladnik:
    def __init__(self, nazwa, ilosc, jednostka):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.jednostka = jednostka

    def __str__(self):
        return f"{self.nazwa}: {self.ilosc} {self.jednostka}"


class Ciasto:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.skladniki = []
        self.kroki = []

    def dodaj_skladnik(self, skladnik):
        self.skladniki.append(skladnik)

    def dodaj_krok(self, opis):
        self.kroki.append(opis)

    def pokaz_przepis(self):
        print(f"\nPrzepis na: {self.nazwa}")
        print("\nSkładniki:")
        for s in self.skladniki:
            print("-", s)

        print("\nKroki:")
        for i, krok in enumerate(self.kroki, 1):
            print(f"{i}. {krok}")

    @staticmethod
    def przelicz_porcje(ilosc, wspolczynnik):
        return ilosc * wspolczynnik


class MalinowaChmurka(Ciasto):
    def __init__(self):
        super().__init__("Malinowa Chmurka")

        # składniki
        self.dodaj_skladnik(Skladnik("herbatniki", 200, "g"))
        self.dodaj_skladnik(Skladnik("maliny", 300, "g"))
        self.dodaj_skladnik(Skladnik("śmietanka 30%", 500, "ml"))
        self.dodaj_skladnik(Skladnik("galaretka malinowa", 2, "szt"))

        # kroki
        self.dodaj_krok("Ułóż herbatniki na spodzie.")
        self.dodaj_krok("Rozpuść galaretkę i dodaj maliny.")
        self.dodaj_krok("Ubij śmietankę.")
        self.dodaj_krok("Połącz wszystko warstwami.")
        self.dodaj_krok("Schłodź w lodówce przez kilka godzin.")


ciasto = MalinowaChmurka()
ciasto.pokaz_przepis()

nowa_ilosc = Ciasto.przelicz_porcje(200, 2)
print("\nPo przeliczeniu porcji herbatników:", nowa_ilosc, "g")
