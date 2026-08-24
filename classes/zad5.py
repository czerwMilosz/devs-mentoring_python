import random

class Card:
    def __init__(self, value: str, suit: str) -> None:
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self) -> None:
       random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            print("No cards left")
            return None

        return self.cards.pop()


def main():
    deck = Deck()

    print("Number of cards:", len(deck.cards))

    deck.shuffle()
    print("Deck shuffled")

    card = deck.deal()
    print("Dealt card:", card)

    print("Cards left:", len(deck.cards))


if __name__ == "__main__":
    main()