import random

class Card(object):
    """this represents one playing card"""
    #class attributes
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    #operator overloading __cmd__ has been depracated use lt, le, eq, etc http://www.programiz.com/python-programming/operator-overloading
    def __lt__(self, other):
        first_card = self.suit, self.rank
        second_card = other.suit, other.rank
        print(first_card)
        return first_card < second_card

class Deck(object):
    """this represents a deck of playing cards"""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_cards(self, num_hands, num_cards_per_hand):
        hands = []
        for i in range(num_hands):
            hand = Hand()
            self.move_cards(hand, num_cards_per_hand)
            hands.append(hand)
        return hands


class Hand(Deck):
    """this is a hand of playing cards, also a child class of the Deck class"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


deck = Deck()
print(deck)



card1 = Card(2, 11)
card2 = Card(3, 2)
print(card2 > card1)