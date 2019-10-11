'''
main.py - Main file to run to play blackjack!
'''
from blackjack import Blackjack
import sys
import time

class Game:
    def __init__(self):
        self.game = Blackjack(6)

    def game_loop(self):
        while True:
            self.game.deal_hands()
            self.display_init_hands()
            bj_check = self.game.blackjack_check()
            if bj_check == True:
                self.blackjack_message()
                self.game.reset_state()
            else:
                for player in self.game.all_players:
                    player.turn = True
                    self.turn_handler()

                self.display_results()
                self.game.reset_state()

    def blackjack_message(self):
        for player in self.game.all_players:
            if player.bj == True:
                print(str(player.id) + ' Blackjack!')
                print(str(player.hand))

    def turn_handler(self):
        for player in self.game.all_players:
            if player.turn == True:
                if player.id == 'User':
                    self.user_selection()
                elif player.id == 'Dealer':
                    self.dealer_hand_loop()
                else:
                    self.AI_hand_display()
                    #self.game.non_user_turn()



    def display_init_hands(self):
        '''Displays the starting hands (dealers 1st card hidden)'''
        print('Dealing Hands...', end='\n\n')
        time.sleep(0.5)
        print('Dealer: ', end=' [')
        print(self.game.dealer.hand[1], end= '] ')
        print(self.game.dealer.hand[1].value)
        time.sleep(0.5)
        print('User: ', end=' ')
        print(self.game.user.hand, end= ' ')
        print(self.game.user.hand.value)
        time.sleep(0.5)

    def display_results(self):
        res = self.game.calc_results()
        if res[3] == 'bust':
            print('Dealer busts!')
        elif res[1] == 'win':
            print(str(res[0]) + ' Wins!', end='\n\n')
        elif res[1] == 'lose':
            print(str(res[0]) + ' Loses!', end='\n\n')
        elif res[1] == 'push':
            print(str(res[0]) + ' Push!', end='\n\n')
        elif res[1] == 'bust':
            print(str(res[0]) + ' Bust!', end='\n\n')


    def blackjack_display(self):
        blackjack = self.blackjack_check()
        if blackjack[0] == True:
            time.sleep(0.5)
            if blackjack[1] == 'push':
                print('PUSH')
            elif blackjack[1] == 'dealer':
                print('Dealer Blackjack, User Loses!')
            elif blackjack[1] == 'blackjack':
                print('User Blackjack, User Wins!')

    def user_selection(self):
        while self.game.user.turn == True:
            print('h - Hit, s - Stand, sp - Split, d - Double Down, q - Quit')
            option = input()
            time.sleep(0.5)
            print('------------' + str(option) + '------------')
            time.sleep(0.5)
            user_option = self.game.user_turn(option)
            if option == 'h':
                print('Hit: ' + str(self.game.user.hand[-1]))
                if self.game.user.action == '21':
                    print('21!')
                elif self.game.user.action == 'bust':
                    print('User Busts!')
            elif user_option == 'double':
                print('Doubling Down: ' + str(self.game.user.hand[-1]))
                if self.game.user.action == '21':
                    print('21!')
                elif self.game.user.action == 'bust':
                    print('User Busts!')
            elif user_option == 's':
                print('Standing')
            elif user_option == 'sp':
                pass

            time.sleep(0.5)
            print('\nDealer: ', end='[')
            print(self.game.dealer.hand[1], end= '] ')
            print(self.game.dealer.hand[1].value)
            time.sleep(0.5)
            print('User: ', end = ' ')
            print(self.game.user.hand, end = ' ')
            print(self.game.user.hand.value, end= '\n\n')
            time.sleep(1.0)

    def display_dealers_hand(self, msg='Dealer: '):
        print(str(msg) + str(self.game.dealer.hand) + \
              ' ' + str(self.game.dealer.hand.value), end='\n\n')



    def dealer_hand_loop(self):
        time.sleep(1.0)
        self.display_dealers_hand('Dealer Shows: ')
        while self.game.dealer.turn == True:
            action = self.game.dealer_turn()
            time.sleep(1.0)
            if action == 'hit':
                print('Dealer Hits: ', end=' ')
                print(self.game.dealer.hand[-1])
                time.sleep(1.0)
                self.display_dealers_hand()
            elif action == 'stand':
                self.display_dealers_hand()
            elif action == 'bust':
                print(self.game.dealer.hand[-1])
                self.display_dealers_hand()
            elif action == '21':
                print(self.game.dealer.hand[-1])
                self.display_dealers_hand()
            elif action =='all_bust':
                self.display_dealers_hand()

        time.sleep(1.0)


if __name__ == '__main__':
    g = Game()
    g.game_loop()
