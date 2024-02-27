#a simple card game
#marko.n@chula.ac.th
#There are 2 players.
#We deal out 2 cards from a deck for both.
#We compare the result. Player1 wins? Player2 wins? Or it's a tie?

class playing_card:
    def __init__(self, suit, value):
        #set a card's suit and value
        self.suit = suit
        self.value = value

    def get_real_val(self):
        #we give the ace (1) higher value than any other card
        if self.value == 1:
            return 14
        return self.value

    def __str__(self):
        return(str(self.value)+" of "+self.suit)

class deck_cards:
    mycards = []
    def __init__(self):
        for suit in ['♠', '♥', '♦', '♣']:
            for card in range(1,14):
                mycard = playing_card(suit, card)
                self.mycards.append(mycard)

    #add: deal a card and remove it from the deck

    def print(self):
        for mycard in self.mycards:
            print(mycard)

mydeck = deck_cards()
#mydeck.print()
#add: deal 2 cards for player1, 2 cards for player2. Which one wins?
#Win criteria: any pair is better than 2 non-pair cards
#If there are 2 pairs, the higher is better. If there are 2 pairs of identical value, it's a tie.
#If there are no pairs, the owner of the highest card wins. If both have .. it's a tie
