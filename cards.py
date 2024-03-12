import random

def create_deck():
    """
    Create a standard deck of playing cards (4 suits, 13 numbers)
    """
    deck = list()
    suits = ["spades", "hearts", "clubs", "diamonds"]
    numbers = ["2", "3", "4", "5", "6", "7", 
               "8", "9", "10", "J", "Q", "K", "A"]
    for suit in suits:
        for number in numbers:
            deck.append((number, suit))
    return deck


def draw_card(deck, n=1):
    """
    Sample n (default 1) cards from a given deck (list of tuples)
    """
    return random.sample(deck, n)


def deal_hands(deck, players=1):
    """
    Output a list of lists of two-card hands from a deck based on the
    number of players (default 1)
    """
    hands = list()
    cards = draw_card(deck, 2 * players)
    for i in range(0, len(cards), 2):
        hands.append([cards[i], cards[i+1]])
    return hands


def remove_card(card, deck):
    """
    Return a new list with a single card (tuple) removed from a deck
    """
    return [x for x in deck if x != card]


def remove_cards(cards, deck):
    """
    Return a new list with some cards (list of tuples) removed from a deck
    """
    return [x for x in deck if x not in cards]


if __name__ == "__main__":
    """
    Test methods
    """
    deck = create_deck()
    print(draw_card(deck, 5))
    print(deal_hands(deck, 5))

    print("\n")
    deck2 = create_deck()
    deck2_removed = []
    for card in deck2:
        if card[1] != "spades":  # Check if the suit is not spades
            deck2_removed.append(card)
    deck2 = remove_cards(deck2_removed, deck2)
    print(deck2)

