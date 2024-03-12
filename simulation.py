from cards import *

# game parameters
num_players = 2

# first 
deck = create_deck()
hands = deal_hands(deck, num_players)
player_1 = hands[0]
player_2 = hands[1]

# eval
print(player_1)