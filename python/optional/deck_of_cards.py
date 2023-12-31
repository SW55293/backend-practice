import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
    
        self.create_deck()
        

    def create_deck(self):
        card_tuple = []
        # card_tuple = (self.RANKS,self.SUITS)

        
        # for x in range(len(self.__cards)):
        #     self.__cards.append(card_tuple)

        for suit in self.SUITS:
            for rank in self.RANKS:
                deck = (rank,suit)
                card_tuple.append(deck)
        self.__cards = card_tuple

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        
        if len(self.__cards) == 0:
            return None

        return self.__cards.pop(0)
    
        

    

    # don't touch below this line
    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"


def test(deck):
    print(deck)
    print("Dealing a hand:")
    hand = []
    for i in range(5):
        card = deck.deal_card()
        if card is None:
            print("Out of cards!")
            break
        print(f" - {card[0]} of {card[1]}")
    print("=====================================")
    return deck


def main():
    random.seed(1)
    deck = DeckOfCards()
    deck.shuffle_deck()
    deck = test(deck)
    deck = test(deck)
    deck = test(deck)


main()
