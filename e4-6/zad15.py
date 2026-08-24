PEOPLE = {
    "90010112345": {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 34,
        "kolor_oczu": "niebieskie"
    },
    "85051254321": {
        "imie": "Anna",
        "nazwisko": "Nowak",
        "wiek": 39,
        "kolor_oczu": "zielone"
    },
    "99030367891": {
        "imie": "Piotr",
        "nazwisko": "Wiśniewski",
        "wiek": 25,
        "kolor_oczu": "brązowe"
    },
    "01071511122": {
        "imie": "Katarzyna",
        "nazwisko": "Wójcik",
        "wiek": 23,
        "kolor_oczu": "szare"
    },
    "92092033344": {
        "imie": "Marek",
        "nazwisko": "Lewandowski",
        "wiek": 31,
        "kolor_oczu": "piwne"
    }
}

def get_mother_name():
    while True:
            mother_name = input("Enter mother name: ").strip().lower()

            if not mother_name.isalpha():
                print("Invalid input")
                continue
            return mother_name.capitalize()


def add_mother_name(dictionary: dict):
    for user_data in dictionary.values():
        user_data["imie_matki"] = get_mother_name()
    return


def delete_invalid_pesel(dictionary: dict):
    for pesel in list(dictionary.keys()):
        if pesel[-1] == "1":
            del dictionary[pesel]
    return dictionary

def print_dictionary(dictionary: dict):
    for pesel, user_data in dictionary.items():
        print(f"\nPesel: {pesel}")
        for key, value in user_data.items():
            print(f"{key}: {value}")

def show_menu():
    return("\n1. Add mother name"
          "\n2. Delete invalid pesel"
          "\n3. Show dictionary"
          "\n4. Exit the program"
          )

def main():
    while True:
        print(show_menu())
        choice = input("Enter your choice: ")
        if choice == "1":
            add_mother_name(PEOPLE)
        elif choice == "2":
            delete_invalid_pesel(PEOPLE)
            print("PESEL numbers ending with '1' have been deleted")
        elif choice == "3":
            print_dictionary(PEOPLE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

