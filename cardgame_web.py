#a simple card game
#marko.n@chula.ac.th
#There are 2 players.
#We deal out 2 cards from a deck for both.
#We compare the result. Player1 wins? Player2 wins? Or it's a tie?
import random

class playing_card:
    def __init__(self, suit, value):
        #set a card's suit and value
        self.suit = suit
        self.value = value
        self.ascii = 127136 + value #spades.. 127137 is the first spade card
        if suit == '♥':
            self.ascii = 127152 + value #hearts, 127153 is the first heart
        if suit == '♦':
            self.ascii = 127168 + value #diamonds, 127169 is the first diamond
        if suit == '♣':
            self.ascii = 127184 + value #clubs, 127185 is the first club

    def get_real_val(self):
        #we give the ace (1) higher value than any other card
        if self.value == 1:
            return 14
        return self.value

    def __str__(self):
        return(str(self.value)+" of "+self.suit+" "+chr(self.ascii))

class deck_cards:
    mycards = []
    def __init__(self):
        for suit in ['♠', '♥', '♦', '♣']:
            for card in range(1,14):
                mycard = playing_card(suit, card)
                self.mycards.append(mycard)

    #add: deal a card and remove it from the deck
    def deal(self):
        #first just get a card from self.mycards
        mycard = random.choice(self.mycards)
        #remove it from the deck so we dont deal it many times
        self.mycards.remove(mycard)
        return(mycard)

    def print(self):
        for mycard in self.mycards:
            print(mycard)

#mydeck = deck_cards()
#mydeck.print()

from flask import Flask

app = Flask(__name__)
#add a card deck into the app
app.deck = deck_cards()

@app.route('/')
def play_cards():
    #deal cards
    p1c1 = app.deck.deal()
    p1c2 = app.deck.deal()
    p2c1 = app.deck.deal()
    p2c2 = app.deck.deal()
    #show them
    ret = "<H1>My cards "+str(p1c1)+" "+str(p1c2)+"<br/>"
    ret = ret + "Computer's cards "+str(p2c1)+" "+str(p2c2)+"</H1>"
    return ret
#add: deal 2 cards for player1, 2 cards for player2. Which one wins?
#Win criteria: any pair is better than 2 non-pair cards
#If there are 2 pairs, the higher is better. If there are 2 pairs of identical value, it's a tie.
#If there are no pairs, the owner of the highest card wins. If both have .. it's a tie

if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
