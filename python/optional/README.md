## **DECK OF CARDS**

A close friend recently contacted you because he knew you can code. His family enjoys playing card games, but their toddler keeps getting into the card drawers and damaging all their playing cards. He asked if you could write a program that would create a deck of playing cards that they could use instead.

#### CHALLENGE
Finish the DeckOfCards class. The SUITS and RANKS of each card have been provided for you as class variables. You won't need to modify them, but you will need to use them.

#### CONSTRUCTOR
Initialize a private empty list called cards.
Fill that empty list by calling the create_deck method within the constructor.
CREATE_DECK(SELF)
This method should create a (Rank, Suit) tuple for all 52 cards in the deck and append them to the cards list.

Order matters! The cards should be appended to the list in the following order: all ranks of hearts, then diamonds, then clubs, and finally spades. Within each suit, the cards should be ordered from lowest rank (Ace) to highest rank (King).

#### SHUFFLE_DECK(SELF)
This method should use the random.shuffle() method (available from the random package) to shuffle the cards in the deck.

#### DEAL_CARD(SELF)
This method should .pop the first card off the top of the deck and return it. If there are no cards left in the deck the method should instead return None.

---
## **THE CALCULATOR**

#### CHALLENGE
Complete the Calculator class.

#### CONSTRUCTOR
Create a private instance variable called result initialized to 0.

#### MATH
The following methods should perform their respective mathematic computations. The "left-hand side" of each operation should be the current value of the result variable. The "right-hand side" of each operation will be the value passed in.

add(self, a)
subtract(self, a)
multiply(self, a)
divide(self, a): If the user attempts to divide by 0, raise a ValueError with "Cannot divide by zero" as the argument
modulo(self, a): If the user attempts to divide by 0, raise a ValueError with "Cannot divide by zero" as the argument
power(self, a):
square_root(self)

#### HELPER METHODS
clear(self): reset the result variable to 0
get_result(self): return the current value stored in the calculator's private result variable.