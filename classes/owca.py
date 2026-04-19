class Owca(object):
    ilosc_nog: int = 4
    ma_siersc: bool = True
    kolor_siersci: str = "bialy"

    def __init__(self, kolor_siersci: str = None):
        self.kolor_siersci = kolor_siersci

    def zmien_kolor_siersci(self, nowy_kolor: str) -> None:
        self.kolor_siersci = nowy_kolor

    @classmethod
    def zmien_ilosc_nog(cls, nowa_ilosc_nog: int) -> None: #metoda klasowa
        cls.ilosc_nog = nowa_ilosc_nog

    @staticmethod
    def czy_to_owca(nazwa: str) -> bool: #metoda statyczna
        return nazwa.lower() == "owca"

Owca.zmien_ilosc_nog(6)
owca_halina = Owca(kolor_siersci= "rozowy")
print(owca_halina.ilosc_nog)
print(owca_halina.kolor_siersci)
print(Owca.ma_siersc)
print(owca_halina.zmien_kolor_siersci(nowy_kolor="czarny"))
print(owca_halina.kolor_siersci)