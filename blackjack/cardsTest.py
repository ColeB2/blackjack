'''Implement tests for every method in hand, card, and deck
sepearate tests for > < and =='''

from cards import Card, Deck, Hand
from colorama import Fore, Style


'''CARD TESTING'''

def card_print_output():
    print( '------: Creating Card')
    print(Fore.CYAN +'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    a = Card('A', 'd')
    print(a)


def card_greater_test():
    '''Testing whether cards are greater/less than or equal too one another'''
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if c > b and b > a and c > a and not a > c and not b > c:
        return True
    else:
        return False

def card_less_test():
    '''Testing whether cards are greater/less than or equal too one another'''
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if a < b and b < c and a < c and not c < a and not c < b:
        return True
    else:
        return False

def card_equal_test():
    '''Testing whether cards are greater/less than or equal too one another'''
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('A', 'h')
    if a == c and c == c and c != b and b != a:
        return True
    else:
        return False

def card_rank_test():
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if a.get_rank() == 'A' and b.get_rank() == '2' and c.get_rank() == ('J'):
        return True
    else:
        return False

def card_suit_test():
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if a.get_suit() == 'd' and b.get_suit() == 'c' and c.get_suit() == ('h'):
        return True
    else:
        return False

def card_face_test():
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if not a.is_face() and not b.is_face() and c.is_face():
        return True
    else:
        return False

def card_ace_test():
    a = Card('A', 'd')
    b = Card('2', 'c')
    c = Card('J', 'h')
    if a.is_ace() and not b.is_ace() and not c.is_ace():
        return True
    else:
        return False

def face_card_rank_test():
    a = Card('A', 'd')
    b = Card('J', 'c')
    c = Card('Q', 'h')
    d = Card('K', 's')
    if a < b < c < d and d > c > b > a:
        return True
    else:
        return False




'''DECK TESTING'''
def deck_print_output():
    print( '------: Creating Deck')
    d = Deck()
    print(Fore.CYAN +'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    deck_iter(d)


def deck_iter(deckObj):
    for card in deckObj:
        print(card, end=' ')
    print()

def deck_card_count_test():
    '''Testing create deck function, that it creates a 52 card deck'''
    d = Deck()
    if d.card_count() == 52:
        return True
    else:
        return False

def deck_shuffle_test():
    '''
    Testing whether shuffle deck function works, by testing it against
    an unshuffled deck
    '''
    a = Deck()
    b = Deck()
    b.shuffle_deck()
    same_spot = 0
    print('------: ' + 'Shuffling Deck')
    print(Fore.CYAN + 'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    deck_iter(b)
    for i in range(a.card_count()):
        if a.cards[i] == b.cards[i]:
            same_spot += 1
    if same_spot == 52:
        return False
    elif same_spot <= 10:
        return True

def deck_remove_top_card_test():
    d = Deck()
    print('------: ' + 'Create Deck')
    print(Fore.CYAN + 'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    deck_iter(d)
    d.remove_top_card()
    print('------: ' + 'Removing Top Card')
    print(Fore.CYAN + 'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    deck_iter(d)
    if d.card_count() == 51:
        return True
    else:
        return False



def deck_deal_to_hand_test():
    '''
    Testing card dealing by dealing 7 cards to 2 separate Hands and
    checking the count of both the cards and hands are correct
    '''
    d = Deck()
    h1 = Hand()
    h2 = Hand()
    for i in range(7):
        d.deal_to_hand(h1)
        d.deal_to_hand(h2)
    if d.card_count() == 38:
        if h1.card_count() == 7 and h2.card_count() == 7:
            return True

def deck_deal_cards_test():
    d = Deck()
    h = Hand()
    d.deal_cards(h, 10)
    if d.card_count() == 42 and h.card_count() == 10:
        return True
    else:
        return False

def deck_reset_deck_test():
    '''
    Reverse the dealing_test(). Deals out the hands, then tests reset functions,
    making sure the deck resets back to a 52 card deck and hands back to 0
    '''
    d = Deck()
    h1 = Hand()
    h2 = Hand()
    for i in range(7):
        d.deal_to_hand(h1)
        d.deal_to_hand(h2)

    if d.card_count() == 38:
        d.reset_deck()
        if h1.card_count() == 7 and h2.card_count() == 7:
            for i in range(h1.card_count()):
                h1.remove_card1()
                h2.remove_card1()
            if h1.is_empty() and h2.is_empty():
                return True
            else:
                print('NOT EMPTY')
                return False
        else:
            print('Doesn\'t have 7 cards')
            return False
    else:
        print('Doesn\'t have 38 cards')
        return False




'''HAND TESTING'''
def hand_print_output():
    print( '------: Creating Hand')
    d = Deck()
    d.shuffle_deck()
    h = Hand()
    d.deal_cards(h, 8)
    print(Fore.CYAN +'OUTPUT: ', end='')
    print(Style.RESET_ALL, end='')
    hand_iter(h)

def hand_iter(handObj):
    for card in handObj:
        print(card, end=' ')
    print()

def hand_card_count_test():
    d = Deck()
    h = Hand()
    d.deal_cards(h, 8)
    if h.card_count() == 8:
        return True
    else:
        return False

def hand_add_card_test():
    c = Card('A', 'd')
    h = Hand()
    h.add_card(c)
    if h.card_count() == 1:
        if h.cards[0].rank == 'A' and h.cards[0].suit == 'd':
            return True
        else:
            return False
    else:
        return False

def hand_remove_card_test():
    c = Card('A', 'd')
    h = Hand()
    h.add_card(c)
    if h.card_count() == 1:
        h.remove_card(-1)
        if h.card_count() == 0:
            return True
        else:
            return False
    else:
        return False

def hand_remove_card1_test():
    c = Card('A', 'd')
    h = Hand()
    h.add_card(c)
    if h.card_count() == 1:
        h.remove_card1()
        if h.card_count() == 0:
            return True
        else:
            return False
    else:
        return False

def hand_is_empty_test():
    c = Card("A", 'd')
    h = Hand()
    if h.is_empty():
        h.add_card(c)
        h.remove_card1()
        if h.is_empty():
            return True
        else:
            return False
    else:
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




if __name__ == '__main__':
    '''Print Output'''
    print('---------------Card Print Output-----------------')
    card_print_output()
    '''Card Testing'''
    print('---------------Card Method Testing---------------')
    TEST(card_greater_test)
    TEST(card_less_test)
    TEST(card_equal_test)
    TEST(card_rank_test)
    TEST(card_suit_test)
    TEST(card_face_test)
    TEST(card_ace_test)
    TEST(face_card_rank_test)


    '''Deck Testing'''
    print('---------------Deck Print Output-----------------')
    deck_print_output()
    print('---------------Deck Method Testing---------------')
    TEST(deck_card_count_test)
    TEST(deck_shuffle_test)
    TEST(deck_remove_top_card_test)
    TEST(deck_deal_to_hand_test)
    TEST(deck_deal_cards_test)
    TEST(deck_reset_deck_test)


    '''Hand Testing'''
    print('---------------Hand Print Output-----------------')
    hand_print_output()
    print('---------------Hand Method Testing---------------')
    TEST(hand_card_count_test)
    TEST(hand_add_card_test)
    TEST(hand_remove_card_test)
    TEST(hand_remove_card1_test)
    TEST(hand_is_empty_test)
