import random

card_names = ["error?", "ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "joker", "queen", "king"]
one_color = [i for i in range(1, 14)]
card_value_plus = [2,3,4,5,6] 
card_value_minus = [0,10,11,12,13]

coins = 10
hand_dealer = []
hand_player = []

class Deck:

    def __init__(self, number_of_decks):
        self.deck_count = 0
        self.number_of_decks = number_of_decks
        self.cards = one_color * 4 * number_of_decks
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        if card in card_value_plus:
            self.deck_count += 1
        elif card in card_value_minus:
            self.deck_count += -1
        return card
    
    def get_true_count(self):
        return round(self.deck_count / (len(self.cards) / 52))


def value_of_hand(cards):    
    cards.sort(reverse=True)
    total = 0
    for value in cards:
        if value == 1 and total < 11:
            total += 11
        elif value > 10:
            total += 10
        else:
            total += value
    
    return total

def over21(value):
    if value > 21:
        return True
    else:
        return False         

def finish_dealer():
    val_dealer = value_of_hand(hand_dealer)
    if val_dealer <= 17:
        hand_dealer.append(deck.draw())
        finish_dealer()
    elif val_dealer > 17 and not over21(val_dealer):
        print("Dealer has:")
        for val in hand_dealer:
            print(card_names[val])
        print("Dealer has {points}".format(points=val_dealer))
    else:
        print("Dealer has:")
        for val in hand_dealer:
            print(card_names[val])
        print("Dealer busted with {points}".format(points=val_dealer))

def deal_round(user_input): 
    if user_input == 'y':
        hand_player.append(deck.draw()) 
        if over21(value_of_hand(hand_player)):
            print("You busted with:")
            for val in hand_player:
                print(card_names[val])
            finish_dealer()
            return False
        else:
            return True
    if user_input == 'd':
        hand_player.append(deck.draw())
        print("You have a {card1}, {card2} and a {card3}".format(card1=card_names[hand_player[0]], card2=card_names[hand_player[1]], card3=card_names[hand_player[2]]))
        finish_dealer()
        return False
    if user_input == 'n':
        finish_dealer()
        return False
    
def end_round(double):
    multiplier = 1
    if double == 'd':
        multiplier = 2

    val_player = value_of_hand(hand_player)
    val_dealer = value_of_hand(hand_dealer)
    
    if not over21(val_player) and (val_player > val_dealer or over21(val_dealer)):
        return 4 * multiplier
    elif val_player == val_dealer:
        print("DRAW!")
        return 2 * multiplier
    elif double == 'd':
        return - 2
    else:
        return 0
        


print("How many decks you want to shuffle for this blackjack round?")
number_of_decks = input()
deck = Deck(int(number_of_decks))
print("You start with 10 coins and the auto bet is 2")

def play_round():
    hand_dealer.append(deck.draw())
    hand_player.append(deck.draw())
    hand_dealer.append(deck.draw())
    hand_player.append(deck.draw())

    print(hand_dealer)
    print("Dealer is showing a {card1}".format(card1=card_names[hand_dealer[0]]))
    print("You have a {card1} and a {card2}. Do you want another or double? (y/n/d)".format(card1=card_names[hand_player[0]], card2=card_names[hand_player[1]]))

    user_input = input()
    another_round_possible = deal_round(user_input)

    if value_of_hand(hand_player) == 21:
        print("BLACKJACK!")
        finish_dealer()
        return 5

    if another_round_possible:
        user_input = input()
        deal_round(user_input)
    
    return end_round(user_input)    

while coins > 1:
    coins = coins - 2
    won = play_round()
    coins = coins + won
    print("You have {coins} coins now!".format(coins=coins))
    hand_dealer = []
    hand_player = []
    if deck.get_true_count() > 6:
        print("The deck is hot!")

    if len(deck.cards) > 8:
        print("{cards} cards are left in the deck!".format(cards=len(deck.cards)))
    else:
        print("Only {cards} cards are left in the deck!".format(cards=len(deck.cards)))
        print("Therefore you finished the deck! Congratulions!")
        break
    
