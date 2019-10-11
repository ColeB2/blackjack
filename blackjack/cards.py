'''cards.py - OOP implementation of a deck of cards'''
from random import shuffle


RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['h', 'c','s','d']

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.val = int()
        self.set_value()
        self.suit_uni = ''
        self.suit_unicode()

    def __str__(self):
        return '{0}{1}'.format(self.rank, self.suit)

    def __repr__(self):
        #return '%s%s' % (self.rank, self.suit)
        return '<{0}.{1} object at {2}>'.format(
                self.__module__, type(self).__name__, hex(id(self)))

    def __lt__(self, other):
        '''Less than operator, comparing card values, Aces considered Low'''
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def suit_unicode(self):
        if self.suit == 'h':
            self.suit_uni = '\u2665'
        elif self.suit == 's':
            self.suit_uni = '\u2660'
        elif self.suit == 'd':
            self.suit_uni = '\u2666'
        elif self.suit == 'c':
            self.suit_uni = '\u2663'


    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def is_face(self):
        '''Checks to see if card is a face card'''
        return self.rank is 'J' or self.rank is 'Q' or self.rank is 'K'

    def is_ace(self):
        '''Checks to see if card is an Ace'''
        return self.rank is 'A'

    def set_value(self):
        '''Sets value of face cards and Ace for comparisons'''
        if self.rank == 'J':
            self.val = 11
        elif self.rank == 'Q':
            self.val = 12
        elif self.rank == 'K':
            self.val = 13
        elif self.rank == 'A':
            self.val = 1
        else:
            self.val = int(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(rank,suit) for rank in RANKS for suit in SUITS]
        self.discards = []

    def __repr__(self):
        return '%s' % (self.cards)

    def __str__(self):
        ret_str = ''
        for card in self.cards:
            ret_str += ''.join([card.rank, card.suit, ' '])
        return ret_str

    def __iter__(self):
        yield from self.cards

    def card_count(self):
        return len(self.cards)

    def shuffle_deck(self):
        return shuffle(self.cards)

    def remove_top_card(self):
        self.discards.append(self.cards[-1])
        return self.cards.pop()

    def deal_to_hand(self, hand_obj):
        '''Deals card from top of deck[-1]'''
        hand_obj.add_card(self.remove_top_card())
        return hand_obj

    def deal_cards(self, hand_obj, num):
        for i in range(num):
            self.deal_to_hand(hand_obj)

    def reset_deck(self):
        for i in range(len(self.discards)):
            self.cards.append(self.discards[-1])
            self.discards.pop()
        self.shuffle_deck()


class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return '%s' % (self.cards)

    def __str__(self):
        ret_str = ''
        for card in self.cards:
            ret_str += ''.join([card.rank, card.suit, ' '])
        return ret_str

    def __getitem__(self, key):
        return self.cards[key]

    def __iter__(self):
        return iter(self.cards)

    def card_count(self):
        return len(self.cards)

    def add_card(self,card):
        self.cards.append(card)
        return card

    def remove_card(self, card):
        self.cards.pop(card)
        return card

    def remove_card1(self):
        self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0
