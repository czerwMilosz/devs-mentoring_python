from dataclasses import dataclass
from typing import Generic, TypeVar, Type
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
    expected_type = object
    def __init__(self):
        self.items = []

    def add(self, item):
        if not isinstance(item, self.expected_type):
            raise ValueError(f"Object must be of type {self.expected_type.__name__}")
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item)

class NoteSubManager(SubManager):
    expected_type = Note

class CardSubManager(SubManager):
    expected_type = Card

T = TypeVar("T") #symbol typu, placeholder
class GenericSubManager(Generic[T]):
    _type: Type[T]
    def __init__(self):
        if not hasattr(self, "_type"):
            raise TypeError("SubManager must have an attribute _type")
        self.items: list[T] = []

    def add(self, item: T) -> None:
        if not isinstance(item, self._type):
            raise TypeError(f"Expected {self._type.__name__}, got {type(item).__name__}")
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item)

class GenericNoteSubManager(GenericSubManager[Note]):
    _type = Note

class GenericCardSubManager(GenericSubManager[Card]):
    _type = Card

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
    # manager = Manager()
    # manager.start()
    card = Card("tttt", "xxx", "dddd")
    subcard = GenericNoteSubManager()
    subcard.add(card)

if __name__ == "__main__":
    main()
