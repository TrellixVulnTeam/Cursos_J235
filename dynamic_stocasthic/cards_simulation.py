import random
import collections

SUITS = ['Sword', 'Heart', 'Diamond', 'Clover']
VALUES = [1 ,2 ,3 , 4, 5, 6, 7, 8, 9, 10, 11, 12,13]

def create_deck():
    deck = []

    for suit in SUITS:
        for value in VALUES:
            deck.append((suit, value))

    return deck


def get_hand(deck, size_hand):
    #random.sample() returns a sample from within a collection without returning
    #the item extracted. Thus we can make sure that a card will not exist twice
    hand = random.sample(deck, size_hand)

    return hand


def main(size_hand, tries):
    deck = create_deck()
    hands = []

    for _ in range(tries):
        hand = get_hand(deck, size_hand)
        hands.append(hand)

    #What's the probability of getting a pair in a hand?
    pairs = 0
    match = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])

        #Using a class from library collections
        counter = dict(collections.Counter(values))
        aux = []

        for val in counter.keys():
            aux.append(val)
            aux.sort()

        ladder = 0

        if len(aux) == size_hand:
            i=0

            while i < len(aux) - 1:
                 if aux[i] + 1 == aux[i + 1]:
                     ladder += 1
                 i += 1

                 if ladder == size_hand - 1:
                     match += 1

    probability = match / tries

    print(f'The probability of getting a ladder in a hand of {size_hand} is of {round(probability*100, 10)}%')


if __name__ == '__main__':
    size_hand = int(input('How many cards does a hand has? '))
    tries = int(input('How many times would you like to run the simulation? '))

    main(size_hand, tries)
