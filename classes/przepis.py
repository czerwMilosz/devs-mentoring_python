class MalinowaChmurka:
    def __init__(self):
        self.skladniki = ["herbatniki", "maliny","śmietana", "galaretka"]
    def pokaz_skladniki(self):
        print("Składniki:")
        for skladnik in self.skladniki:
            print("-", skladnik)

    @staticmethod
    def przelicz(ilosc, razy):
        return ilosc * razy

ciasto = MalinowaChmurka()
ciasto.pokaz_skladniki()
print("Podwojna ilosc malin:",MalinowaChmurka.przelicz(200, 2), "g")