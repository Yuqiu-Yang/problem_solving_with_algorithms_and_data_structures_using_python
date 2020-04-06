from random import shuffle
class pokerCard(object):
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def __str__(self):
        return f'{self.number} of {self.suit}'

class cardDeck(object):
    def __init__(self):
        self.deck = []
        self.num = len(self.deck)
    def addCard(self,card,index):
        self.deck.insert(index, card)
    def shuffleDeck(self):
        temp = list(range(self.num))
        shuffle(temp)
        tempDeck = [self.deck[i] for i in temp]
        self.deck = tempDeck
    def drawCard(self):
        return self.deck.pop()
