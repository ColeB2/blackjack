'''
bj.py - OOP Implementation of Black Jack!
Underlying Game Logic and Rules needed to play Black Jack!
#TODO; HANDLE USER HAND VALUE and LOGIC and WIN CONDITIOONS
'''
from blackjackcards import BlackjackHand, BlackjackCard, BlackjackDeck
from blackjackplayers import User, Dealer
import sys
import time

class Blackjack:
    def __init__(self, num_decks=6):
        self.num_decks = num_decks
        self.deck = BlackjackDeck(self.num_decks)
        self.deck.shuffle_deck()
        self.user = User()
        self.dealer = Dealer()
        self.all_players = [self.user, self.dealer]
        self.all_players[0].turn = True
        for i in range(1, len(self.all_players[1:]), 1):
            self.all_players[i].turn = False
        self.players = [self.user]

    def deal_hands(self):
        self.deck.blackjack_shuffle()
        self.all_players[0].turn = True
        for i in range(2):
            for player in self.all_players:
                self.deck.deal_to_hand(player.hand)
        for player in self.all_players:
            player.hand.hand_value()

    def blackjack_check(self):
        for player in self.players:
            if player.hand.value == 21:
                player.bj = True
                if self.dealer.hand.value == 21:
                    self.dealer.bj = True
                    #return Bets
                    return (True, 'PUSH')
                else:
                    #Receive payout
                    return (True)
        if self.dealer.hand.value == 21:
            self.dealer.bj = True
            #take money
            return (True)
        return (False)

    def user_turn(self, option):
        if option.lower() == 'q':
            sys.exit()
        elif option.lower() == 'h':
            self.user.hit(self.deck)
            return (self.user.hand, self.user.hand[-1])
        elif option.lower() == 's':
            self.user.stand()
            return (self.user.hand)
        elif option.lower() == 'sp':
            self.user.split_options()
            return (self.user.hand, self.user.hand[-1])
        elif option.lower() == 'd':
            self.user.double_down(self.deck)
            return (self.user.hand, self.user.hand[-1])

    def dealer_turn(self):
        all_busted = False
        while self.dealer.turn == True:
            for player in self.players:
                if player.action != 'bust':
                    #if not all players are busted, break, continue dealer turn
                    all_busted = False
                    break
                else:
                    all_busted = True
            if all_busted == False:
                if self.dealer.hand.value < 17:
                    self.dealer.hit(self.deck)
                    return self.dealer.action
                elif self.dealer.hand.value >= 17:
                    self.dealer.stand()
                    return self.dealer.action
                elif self.dealer.hand.value > 21:
                    return self.dealer.action
            else:
                self.dealer.stand()
                return 'all_bust'

    def AI_turn(self):
        '''Implement in future to add other AI/CPU players'''
        pass


    def calc_results(self):
        for player in self.players:
            if player.hand.value <= 21 and self.dealer.hand.value <=21:
                if player.hand.value > self.dealer.hand.value:
                    return (player.id, 'win', 'dealer', 'lose')
                elif player.hand.value < self.dealer.hand.value:
                    return (player.id, 'lose', 'dealer', 'win')
                elif player.hand.value == self.dealer.hand.value:
                    return (player.id, 'push', 'dealer', 'push')
            elif player.hand.value > 21 and self.dealer.hand.value <=21:
                return (player.id, 'bust', 'dealer', 'win')
            elif player.hand.value < 21 and self.dealer.hand.value >21:
                return (player.id, 'win', 'dealer', 'bust')


    def reset_state(self):
        for player in self.all_players:
            player.hand.discard_hand()
            player.bj = False
            player.turn = False
