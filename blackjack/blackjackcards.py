'''
blackjackcards.py - extention of classes of myCards.py with functionality
for a black jack game
'''
from cards import Card, Deck, Hand


RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['h', 'c','s','d']


class BlackjackCard(Card):
    def __init__(self, rank, suit):
        Card.__init__(self, rank, suit)
        self.value = int()
        self.card_value()

    def card_value(self):
        '''Sets the Blackjack value of each card
        2-9 = face value, JQK = 10 and A = 1/11'''
        if self.is_face():
            self.value = 10
        elif self.is_ace():
            self.value = (1, 11)
        else:
            self.value = int(self.rank)
        return self.value

class BlackjackDeck(Deck):
    def __init__(self, num_decks=6):
        Deck.__init__(self)
        self.num_decks = num_decks
        self.cards = []
        self.create_deck()
        self.discards = []

    def create_deck(self):
        '''Creates a blackjack deck based on num_deck specified
        at creation of class'''
        for i in range(self.num_decks):
            self.cards += [BlackjackCard(rank,suit) for rank in RANKS for suit in SUITS]

    def blackjack_shuffle(self):
        '''Method that shuffles the deck once 75% of cards are used'''
        ratio_left = len(self.discards)/(self.num_decks*52)
        if ratio_left >= 0.75:
            self.reset_deck()
            return True

    def discard(self, x):
        '''Method to discard x # of cards to the discards list
        used for testing purposes'''
        for i in range(x):
            self.remove_top_card()


class BlackjackHand(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.value = int()

    def ace_check(self):
        '''Checks to see if starting Hand(first 2 cards) contains an Ace'''
        for card in self.cards:
            if card.is_ace():
                return True
        return False

    def hand_value(self):
        '''Calculates the value of a Blackjack Hand'''
        has_ace = self.ace_check()
        if self.card_count() > 2 and has_ace:
            self.handle_ace()
        elif self.card_count() > 2 and not has_ace:
            if self.cards[-1].is_ace():
                self.handle_ace()
            else:
                self.value += self.cards[-1].value
        else:
            for card in self.cards:
                if card.is_ace():
                    self.handle_ace()
                    break
                else:
                    self.value += card.value

    def handle_ace(self):
        '''Handles value of 'Ace' Card'''
        self.value = 0
        for card in self.cards:
            if card.is_ace():
                if self.value + 11 > 21:
                    self.value += 1
                else:
                    self.value += 11
            else:
                self.value += card.value
        '''Checks to see if >21, change value of previous Aces'''
        if self.value > 21:
            self.value = 0
            for card in self.cards:
                if card.is_ace():
                    self.value += 1
                else:
                    self.value += card.value

    def discard_hand(self):
        while len(self.cards) != 0:
            self.remove_card1()
        self.value = 0
