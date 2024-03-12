from collections import defaultdict 
def validate_hand(hand):
    """
    Raise exception if there are duplicate cards in a hand
    """
    if len(hand) != len(set(hand)):
        raise Exception("Hand contains duplicate cards")

def best_hand(hand):
    """
    Output the best 5-card poker hand from a list of cards in a hand
    """
    pass


def number_hand(hand):
    """
    Outputs if a hand has four-of-a-kind, triples, two pair, pair,
    or high card
    """
    number_count = defaultdict(int)
    for card in hand:
        number = card[0]
        number_count[number] += 1
    
    hasTriple = False
    hasPair = False
    for count in number_count.values():
        if count == 4:
            return "four-of-a-kind"
        if count == 3:
            hasTriple = True
            if hasPair:
                return "full house"
        if count == 2:
            hasPair = True
            if hasPair:
                return "two pair"
    
    if hasTriple:
        return "triple"
    elif hasPair:
        return "pair"
    else:
        return "high card"


def has_flush(hand):
    """
    Outputs if a hand has a flush
    """
    suit_count = defaultdict(int)
    for card in hand:
        suit = card[1]
        suit_count[suit] += 1
    for count in suit_count.values():
        if count >= 5:
            return True
    return False


def has_straight(hand):
    """
    Outputs if a hand has a straight
    """
    


def winner(hand1, hand2):
    """
    Output the winner given two hands
    """
    pass


if __name__ == "__main__":
    """
    Test methods
    """
    hand = [('J', 'spades'), ('2', 'spades'), ('J', 'diamonds'), ('2', 'diamonds'), ('6', 'spades')]
    validate_hand(hand)
    # print(number_hand(hand))
    has_flush(hand)