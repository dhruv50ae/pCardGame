from random import shuffle

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        self.allCards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allCards)

    def splitInHalf(self):
        return (self.allCards[:26], self.allCards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return f"Contains {len(self.cards)} cards"

    def add(self, addedCards):
        self.cards.extend(addedCards)

    def removeCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def playCard(self):
        drawnCard = self.hand.removeCard()
        print(f"{self.name} has placed: {drawnCard}\n")
        return drawnCard

    def removeWarCard(self):
        warCards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                warCards.append(self.hand.cards.pop())
                return warCards

    def stillHasCards(self):
        return len(self.hand.cards) != 0


print("Welcome to War (the card game), let's begin...\n")

d = Deck()
d.shuffle()
half1, half2 = d.splitInHalf()
comp = Player("Computer", Hand(half1))
name = input("Enter your name to begin: ")
user = Player(name, Hand(half2))
totalRounds = 0
warCount = 0
while user.stillHasCards() and comp.stillHasCards():
    totalRounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(f"{user.name} has the count: {len(user.hand.cards)}")
    print(f"{comp.name} has the count: {len(comp.hand.cards)}")
    print("Play a card! \n")
    tableCards = []
    cCard = comp.playCard()
    pCard = user.playCard()
    tableCards.append(cCard)
    tableCards.append(pCard)
    if cCard[1] == pCard[1]:
        warCount += 1
        print("War!")
        tableCards.extend(user.removeWarCard())
        tableCards.extend(comp.removeWarCard())
        if RANKS.index(cCard[1]) < RANKS.index(pCard[1]):
            user.hand.add(tableCards)
        else:
            comp.hand.add(tableCards)
    else:
        if RANKS.index(cCard[1]) < RANKS.index(pCard[1]):
            user.hand.add(tableCards)
        else:
            comp.hand.add(tableCards)
print(f"Game over. Number of rounds: {totalRounds}")
print(f"A war happened {warCount} times")
