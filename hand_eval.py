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
    # Cannot make straight automatically
    if len(hand) < 5:
        return False
    
    nums = set()
    for card in hand:
        val = card[0]
        number = int()
        if val == "J":
            nums.add(11)
        elif val == "Q":
            nums.add(12)
        elif val == "K":
            nums.add(13)
        elif val == "A":
            nums.add(1)
            nums.add(14)
        else:
            number = int(val)
            nums.add(number)
        
    sortedNums = sorted(list(nums))
    N = len(sortedNums)
    for i in range(N):
        # cannot make a straight with remaining cards
        if (i + 5 > N):
            return False
        # brute force: check if numbers are consecutive
        for j in range(4):
            if sortedNums[i + j] + 1 != sortedNums[i + j + 1]:
                return False

        return True


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
    hand2 = [('6', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades')]
    print(hand)
    validate_hand(hand)
    print(number_hand(hand))    # two pair
    print(has_flush(hand))      # False
    print(has_flush(hand2))     # True
    print(has_straight(hand2))  # True