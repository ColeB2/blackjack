'''
bjplayers.py - Classes of User, and Dealer for a game of BlackJack
TODO: Update Return values to complete their Contract!
'''
from blackjackcards import BlackjackCard, BlackjackDeck, BlackjackHand
import sys

class User:
    def __init__(self):
        self.hand = BlackjackHand()
        self.turn = True
        self.bj = False
        self.id = 'User'
        self.action = ''

    def hit(self, deck_obj):
        self.action = 'hit'
        deck_obj.deal_to_hand(self.hand)
        self.hand.hand_value()
        self.handle_new_card()
        return (self.action, self.hand.cards[-1], self.hand, self.hand.value)

    def stand(self):
        self.action = 'stand'
        self.turn = False
        return (self.action, self.hand, self.hand.value)

    def split(self):
        ##Implement later
        self.action = 'split'
        raise NotImplemented
        self.split_hand = True
        self.hand2.add_card(self.hand[1])
        self.hand.remove_card1()
        self.hand.hand_value()
        self.hand2.hand_value()
        return (self.action)

    def double_down(self, deck_obj):
        #double Bet, hit once, end turn
        self.action = 'double'
        deck_obj.deal_to_hand(self.hand)
        self.hand.hand_value()
        self.handle_new_card()
        return (self.action, self.hand.cards[-1], self.hand,  self.hand.value)

    def handle_new_card(self):
        if self.hand.value == 21:
            self.action = '21'
            self.turn = False
        elif self.hand.value >= 21:
            self.action = 'bust'
            self.turn = False


class Dealer(User):
    def __init__(self):
        self.hand = BlackjackHand()
        self.turn = False
        self.bj = False
        self.id = 'Dealer'
        self.action = ''
