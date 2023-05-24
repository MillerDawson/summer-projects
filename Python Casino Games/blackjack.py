import cards

class Blackjack(object):
    dealer_hand = []
    player_hand = []

    def play(self):
        """ The main play function for Blackjack """
        card_deck = cards.Deck()
        card_deck.shuffle_deck()
        inplay = True

        while inplay == True:
            Blackjack().dealer_hand.append(card_deck.draw_card())
            Blackjack().player_hand.append(card_deck.draw_card())
            Blackjack().dealer_hand.append(card_deck.draw_card())
            Blackjack().player_hand.append(card_deck.draw_card())

            print(f" Dealer Shows: {Blackjack().dealer_hand[0]}")
            print(f" Player Shows: {Blackjack().player_hand} ==> {Blackjack().player_hand_value()}")
            inplay = False

    def player_hand_value(self) -> int:
        """ Returns the integer value of players hand """
        total = 0
        for card in Blackjack().player_hand:
            if card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                total += 10
            elif card[1] == 'A':
                total += 11
            else:
                total += int(card[1])
        return total

    def dealer_hand_value(self) -> int:
        """ Returns the integer value of dealers hand """
        total = 0
        for card in Blackjack().dealer_hand:
            if card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                total += 10
            elif card[1] == 'A':
                total += 11
            else:
                total += int(card[1])
        return total

Blackjack().play()
