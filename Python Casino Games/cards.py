from random import shuffle

class Deck(object):
    def __init__(self) -> None:
        """ Initialiser for Deck class"""
        self.cards = []
        self.create_deck()

    def __str__(self) -> str:
        """ Returns the string value of the current card deck"""
        return str(self.cards)

    def __len__(self) -> int:
        """ Returns how many cards are in a Deck """
        return len(self.cards)

    def create_deck(self) -> None:
        """ Creates the card deck and stores it in self.cards """
        for i in Card.card_suit:
            for j in Card.card_value:
                self.cards.append([i, j])

    def shuffle_deck(self) -> None:
        """ Shuffles the cards """
        shuffle(self.cards)

    def draw_card(self) -> list:
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            # could create custom class exception here
            print("The deck is empty")
            return None

class Card(Deck):
    """ Card Class - A child of the Deck class """
    card_value = ['A', '2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K']
    card_suit = ["Heart", "Club", "Spade", "Diamond"]

if __name__ == "__main__":
    # some testing for cards
    x = Deck()
    print(len(x.cards))
    x.shuffle_deck()
    print(x.cards)

    x.draw_card()
    x.draw_card()