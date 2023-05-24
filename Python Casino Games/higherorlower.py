import cards

class higher_or_lower(object):
    """ main class for unlimited higher or lower game """

    def __init__(self) -> None:
        self.player_choice = None
        self.streak = 0
        self.playing = False

    def play(self) -> None:
        """ The main play function for Blackjack """
        self.playing = True 

        self.card_deck = cards.Deck() # creates the deck
        self.card_deck.shuffle_deck()
        card = self.card_deck.draw_card() # draws your card from the deck


        while self.playing == True: # the loop for the infinite play of the game
            self.card_deck = cards.Deck() # recreates the deck everytime for endless higher or lower
            self.card_deck.shuffle_deck()
            
            self.player_choice = input(f"Your card is: {card}, do you think the next card is h or l:\n")
            player_card = self.get_card_value(card) # gets the value of the player card

            card = self.card_deck.draw_card() # draws the compare card from the deck
            next_card = self.get_card_value(card) # gets value of the compare card

            self.get_result(player_card, next_card) # gets the result of the card


    def get_card_value(self, card) -> int:
        if card[1] == 'J' or card[1] == 'Q' or card[1] ==  'K':
            return 10
        elif card[1] == 'A':
            return 11
        else:
            return int(card[1])

    def get_result(self, player_card:int, next_card:int) -> int:
        if self.player_choice == 'h':
            if next_card >= player_card:
                print(f"Correct - next card was {next_card}")
                self.streak +=1
                return self.streak
            else:
                print(f"Incorrect - next card was {next_card}")
                self.playing = False
                return self.streak
        else:
            if next_card <= player_card:
                print(f"Correct - next card was {next_card}")
                self.streak +=1
                return self.streak
            else:
                print(f"Incorrect - next card was {next_card}")
                self.playing = False
                return self.streak


higher_or_lower().play()