'''Cards, anay.taparia@gmail.com'''
import random
# define constants
SUITS = "♠♡♢♣"
HEART = "♡"
DIAMOND = "♢"
CLUB = "♣"
SPADE = "♠"
NUMBERS = list("A23456789JQK")
NUMBERS.append("10")
NUM_OF_JOKERS = 2
class Card:
    """A card."""
    def __init__(self,suit,num,face_down=True,joker=False):
        self.suit = suit
        self.num = num
        self.fd = face_down
        self.joker = joker

    def __str__(self):
        if self.fd:
            return """
+--+
|##|
|##|
+--+""".strip()
        elif self.joker:
            return """
+--+
|jo|
|ke|
+--+""".strip()
        else:
            return """
+--+
|{} |
|{}|
+--+""".format(self.suit,self.num.rjust(2)).strip()
        
class Deck:
    '''A deck of cards.'''
    def __init__(self,facedown=True):
        self.cards = []
        for suit in SUITS:
            for num in NUMBERS:
                self.cards.append(Card(suit,num,facedown))
        for _ in range(NUM_OF_JOKERS):
            self.cards.append(Card(suit,num,facedown,joker=True))
        random.shuffle(self.cards)

def split_deck(deck, stack_1):
    '''Splits the deck into a stack of stack_1'''
    deck = deck.cards
    return deck[:stack_1],deck[stack_1:]
