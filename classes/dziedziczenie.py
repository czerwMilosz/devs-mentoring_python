class Zwierze:
    def dzwiek(self):
        print("jakis dzwiek")

class Kot(Zwierze):
    # def dzwiek(self):
    #     print("miau")
    pass

class Owca(Kot, Zwierze):
    # def dzwiek(self):
    #     print("bee")
    pass

kot = Kot()
kot.dzwiek()
owca = Owca()
owca.dzwiek()
print(Owca.mro())