import cards
import hand_eval

# game parameters
num_players = 2

# dealing first 2 
deck = cards.create_deck()
hands = cards.deal_hands(deck, num_players)
deck = cards.remove_cards(hands, deck)

hand1 = hands[0]
hand2 = hands[1]

h1_eval = hand_eval.best_hand(hand1)
h2_eval = hand_eval.best_hand(hand2)

print(h1_eval)
print(h2_eval)

# flop
flop = cards.draw_card(deck, 3)
deck = cards.remove_cards(flop, deck)

hand1 = hand1 + flop
hand2 = hand2 + flop

h1_eval = hand_eval.best_hand(hand1)
h2_eval = hand_eval.best_hand(hand2)

print(h1_eval)
print(h2_eval)

# turn
turn = cards.draw_card(deck)
deck = cards.remove_cards(turn, deck)
hand1 = hand1 + turn
hand2 = hand2 + turn

h1_eval = hand_eval.best_hand(hand1)
h2_eval = hand_eval.best_hand(hand2)

print(h1_eval)
print(h2_eval)

# river
river = cards.draw_card(deck)
deck = cards.remove_cards(river, deck)

hand1 = hand1 + river
hand2 = hand2 + river

h1_eval = hand_eval.best_hand(hand1)
h2_eval = hand_eval.best_hand(hand2)

print(h1_eval)
print(h2_eval)
