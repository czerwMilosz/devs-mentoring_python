import string
DEFINITIONS = {'kos' : 'Turdus merula',
               'wilga' : 'Oriolus oriolus',
               'rudzik' : 'Erithacus rubecula',
               'kukulka' : 'Cuculus canorus',
               'pleszka' : 'Phoenicurus phoenicurus',
               'bogatka' : 'Parus major',
               'drozd' : 'Turdus philomelos',
               'zieba' : 'Fringilla coelebs',
               'dzwoniec' : 'Chloris chloris',
               'szczygiel' : 'Carduelis carduelis',
               'szpak' : 'Sturnus vulgaris',
               'kopciuszek' : 'Phoenicurus ochruros'}

TEXT = ("W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, "
        "po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. "
        "Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, "
        "swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje "
        "swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, "
        "a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie "
        "okazuja sie byc dzwoniec i szczygiel.")

def add_definition(text: str, definitions: dict):
    split_text = text.split()
    new_text = ""
    for word in split_text:
        if word.strip(string.punctuation).lower() in definitions:
            stripped_word = word.strip(string.punctuation)
            new_text += (
                    stripped_word + " " +
                    f"({definitions[stripped_word.lower()]})" +
                    f"{word.strip(string.ascii_letters)}" + " ") # dodaje znaki interpuncyjne jesli istnieja
        else:
            new_text += word + " "

    return new_text


def main():
    print(add_definition(TEXT, DEFINITIONS))

if __name__ == "__main__":
    main()

