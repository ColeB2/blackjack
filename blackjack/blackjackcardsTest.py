'''Test for blackjackcards.py
Current Version
'''

from blackjackcards import BlackjackHand, BlackjackCard, BlackjackDeck
from colorama import Fore, Style

'''BLACKJACK CARD CLASS TESTING'''
def card_value_test():
    a = BlackjackCard('8','h')
    b = BlackjackCard('A', 'h')
    c = BlackjackCard('J', 'c')
    d = BlackjackCard('K', 'd')
    if a.value == 8 and b.value == (1,11) and c.value == 10 and d.value == 10:
        return True
    else:
        return False


'''BLACKJACK HAND TESTING'''
def hand_card_value_test(c1, c2, ev, c3=None, ev2=None, c4=None, ev3=None):
    hand = BlackjackHand()
    A = BlackjackCard(c1[0], c1[1])
    B = BlackjackCard(c2[0], c2[1])
    hand.add_card(A)
    hand.add_card(B)
    hand.hand_value()
    if c3 == None:
        if hand.value == ev:
            return (True, hand.value, c1, c2, ev, c3, c4)
        else:
            return (False, hand.value, c1, c2, ev, c3, c4)
    elif c3 != None:
        if hand.value == ev:
            C = BlackjackCard(c3[0], c3[1])
            hand.add_card(C)
            hand.hand_value()
            if c4 == None:
                if hand.value == ev2:
                    return (True, hand.value, c1, c2, ev2, c3, c4)
                else:
                    return (False, hand.value, c1, c2, ev2, c3, c4)
            elif c4 != None:
                if hand.value == ev2:
                    D = BlackjackCard(c4[0], c4[1])
                    hand.add_card(D)
                    hand.hand_value()
                    if hand.value == ev3:
                        return (True, hand.value, c1, c2, ev3, c3, c4)
                    else:
                        return (False, hand.value, c1, c2, ev3, c3, c4)
                else:
                    return (False, hand.value, c1, c2, ev, c3, c4)
        else:
            return (False, hand.value, c1, c2, ev, c3, c4)






'''BLACKJACK DECK TESTING'''
def deck_size_test():
    '''Checks than in a 6 deck shoe, 24 7s exist'''
    c = BlackjackCard('7', 'd')
    d = BlackjackDeck(6)
    count = 0
    for card in d:
        if card == c:
            count += 1
    if count == 24:
        return True
    else:
        return False

def deck_shuffle_test():
    '''Checks that deck shuffles shoe at ratio 75% (234/312 for 6 deck)'''
    d = BlackjackDeck(6)
    for i in range(6*52):
        d.discard(1)
        shuffled = d.blackjack_shuffle()
        if shuffled == True:
            return True
    return False





def TEST(testFunc):
    if testFunc() == True:
        print(Fore.GREEN + 'Passed:', end=' ')
        print(Style.RESET_ALL, end='')
        print(str(testFunc))
    else:
        print(Fore.RED + 'Failed:', end=' ')
        print(Style.RESET_ALL, end='')
        print(str(testFunc))

def HANDTEST(testFunc):
    if testFunc[0] == True:
        print(Fore.GREEN + 'Passed:', end=' ')
        print(Style.RESET_ALL, end='')
        print('Hand: ' + str(testFunc[2]) + ' ' + str(testFunc[3]) + ' ' + \
              'Hit Card(s): ' + str(testFunc[5]) + ' ' + \
                              str(testFunc[6]) + ' ' + \
              'Value: ' + str(testFunc[1]) + ' ' + \
              'Expected Value: ' + str(testFunc[4])     )
    else:
        print(Fore.RED + 'Failed:', end=' ')
        print(Style.RESET_ALL, end='')
        print('Hand: ' + str(testFunc[2]) + ' ' + str(testFunc[3]) + ' ' + \
              'Hit Card(s): ' + str(testFunc[5]) + ' ' + \
                                str(testFunc[6]) + ' ' + \
              'Value: ' + str(testFunc[1]) + ' ' + \
              'Expected Value: ' + str(testFunc[4]) )

if __name__ == '__main__':
    '''Testing BlackjackCard Methods'''
    TEST(card_value_test)
    '''Testing BlackjackDeck Methods'''
    TEST(deck_size_test)
    TEST(deck_shuffle_test)
    '''Testing BlackjackHand Values'''
    HANDTEST(hand_card_value_test('8h', 'Ah', 19))
    HANDTEST(hand_card_value_test('Ah', '3c', 14))
    HANDTEST(hand_card_value_test('Ad', 'Ah', 12))
    HANDTEST(hand_card_value_test('Ad', 'Ah', 12, 'Ac', 13))
    HANDTEST(hand_card_value_test('Ad', 'Ah', 12, '2c', 14))
    HANDTEST(hand_card_value_test('Ad', 'Ah', 12, 'Kd', 12))
    HANDTEST(hand_card_value_test('Ad', 'Ah', 12, 'Ac', 13, 'Ks', 13))
