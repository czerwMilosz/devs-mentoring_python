from dataclasses import dataclass

@dataclass
class Note:
    title: str
    content: str

@dataclass
class Card:
    name: str
    phone: str
    email: str

class SubManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item)

class NoteSubManager(SubManager):
    def add(self, note:Note):
        if not isinstance(note, Note):
            raise ValueError("Object must be of type Note")
        super().add(note)

class CardSubManager(SubManager):
    def add(self, card:Card):
        if not isinstance(card, Card):
            raise ValueError("Object must be of type Card")
        super().add(card)

class Menu:
    def show(self):
        print(f"\n1. Dodaj notatkę"
              f"\n2. Dodaj wizytówkę (Card)"
              f"\n3. Wyświetl wszystkie notatki"
              f"\n4. Wyświetl wszystkie wizytówki"
              f"\n5. Wyjdź")

    def get_choice(self):
        return input("Wybierz opcję: ")

class Manager:
    def __init__(self):
        self.menu = Menu()
        self.notes_manager = NoteSubManager()
        self.cards_manager = CardSubManager()

    def start(self):
        while True:
            self.show_menu()
            choice = self.execute()

            if choice == "5":
                print("Koniec programu.")
                break

    def show_menu(self):
        self.menu.show()

    def execute(self):
        choice = self.menu.get_choice()

        if choice == "1":
            title = input("Podaj tytuł notatki: ")
            content = input("Podaj treść notatki: ")

            note = Note(title, content)
            self.notes_manager.add(note)

        elif choice == "2":
            name = input("Podaj imię: ")
            phone = input("Podaj telefon: ")
            email = input("Podaj email: ")

            card = Card(name, phone, email)
            self.cards_manager.add(card)

        elif choice == "3":
            self.show_notes()

        elif choice == "4":
            self.show_cards()

        elif choice == "5":
            return choice

        else:
            print("Niepoprawny wybór.")

        return choice

    def show_notes(self):
        self.notes_manager.show()

    def show_cards(self):
        self.cards_manager.show()



def main():
    manager = Manager()
    manager.start()

if __name__ == "__main__":
    main()
