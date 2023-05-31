import cards

class Blackjack(object):
    def __init__(self) -> None:
        self.card_deck = cards.Deck()
        self.card_deck.shuffle_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.split_hands = []
        self.split_amount = 2 # can adjust the split amount - right now max split of 2 times
    
    def deal_cards(self):
        """ Deals two cards to the player and dealer """
        for i in range(2):
            self.player_hand.append(['Diamond', 'A']) # debug splits        
            
            #self.player_hand.append(self.card_deck.draw_card())
            self.dealer_hand.append(self.card_deck.draw_card())
            self.check_split()
    
    def display_hands(self):
        """ Prints both player and dealer hands """
        print(f"Player hand: {self.player_hand}\nDealer hand: {self.dealer_hand[:1]}")
    
    def player_turn(self):
        """ The player's turn """
        while True:
            self.display_hands()
            choice = input("Would you like to hit or stand? (h/s): ")
            if choice.lower() == 'h':
                self.player_hand.append(self.card_deck.draw_card())
                if self.get_card_value(self.player_hand) > 21:
                    print("Player busts!")
                    return
            elif choice.lower() == 's':
                return
            else:
                print("Invalid input. Please enter h or s.")
                
    def dealer_turn(self):
        """ The dealer's turn """
        while self.get_card_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.card_deck.draw_card())
        if self.get_card_value(self.dealer_hand) > 21:
            print("Dealer busts!")

    def get_card_value(self, hand) -> int:
        """ Returns the integer value of a hand """
        total = 0
        aces = 0 # must keep count of aces
        for card in hand:
            if card[1] in ['J', 'Q', 'K']:
                total += 10
            elif card[1] == 'A':
                total += 11
                aces+=1
            else:
                total += int(card[1])
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    def check_split(self):
        """ Checks if the player can split their hand """
        if len(self.player_hand) == 2 and self.player_hand[0][1] == self.player_hand[1][1] and len(self.split_hands) < self.split_amount:
            self.display_hands()
            choice = input("Would you like to split your hand? (y/n): ")
            if choice.lower() == 'y':
                current_split_hand = [self.player_hand.pop()]
                # split_hand.append(self.card_deck.draw_card())
                current_split_hand.append(['Diamond', 'A'])
                self.split_hands.append(current_split_hand)
                self.player_hand.append(self.card_deck.draw_card())
                self.play_split_hands()
    
    def play_split_hands(self):
        """ Plays the split hands """
        for hand in self.split_hands:
            while True:
                print(f"Split hand: {hand}\nDealer hand: {self.dealer_hand[:1]}")
                choice = input("Would you like to hit or stand? (h/s): ")
                if choice.lower() == 'h':
                    hand.append(self.card_deck.draw_card())
                    if self.get_card_value(hand) > 21:
                        print("Split hand busts!")
                        break
                elif choice.lower() == 's':
                    break
                else:
                    print("Invalid input. Please enter h or s.")
    
    def check_winner_helper(self, val, dealer_score):
        """ Helper for the check_winner function - prints winner result """
        if val > 21:
            print(f"Player's Hand busts!")
        elif dealer_score > 21 or val > dealer_score:
            print(f"Player's hand wins!")
        elif dealer_score > val:
            print(f"Dealer's hand wins :(")
        else:
            print(f"It's a push!")

    def check_winner(self):
        """ Checks who the winner is for every hand """
        player_score = self.get_card_value(self.player_hand)
        dealer_score = self.get_card_value(self.dealer_hand)
        
        print(f"Dealer hand: {self.dealer_hand} | Dealer hand value: {dealer_score}")
        if len(self.split_hands) > 0:
            for hand in self.split_hands:
                split_hand_score = self.get_card_value(hand)
                print(f"Split hand: {hand} | Split hand value: {split_hand_score}")
                self.check_winner_helper(split_hand_score, dealer_score)
        
        print(f"Player hand: {self.player_hand} | Your hand value: {player_score}")
        self.check_winner_helper(player_score, dealer_score)

    def play(self):
        """ The main play function for Blackjack """
        bj = Blackjack()
        bj.deal_cards()
        bj.player_turn()
        bj.dealer_turn()
        bj.check_winner()

if __name__ == "__main__":
    game = Blackjack().play()



"""
Doesn't allow resplit if you've split 1 hand already 
 
Doesn't play all split hands, only plays 1 split hand

Make it so dealer auto wins if it has ace_ and face/10 cards, same with player

Official Game additions:
Add a double down feature
Change how the cards are displayed
Make it so that if dealer has ace offers insurance
Blackjack pay 3:2 in official game
"""

# Doesn't show dealer card value at any point
# Add a function which will display both hands 
# Doesn't show split card value
# Display all played hands in the check_winner function, currently not showing split hands and only 1 player hand
