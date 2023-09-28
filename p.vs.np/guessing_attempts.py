'''
Complete the get_num_guesses function. It takes a password length as input and returns the number of 
guesses required to ensure that a password of that length is guessed.

THE GUESSING STRATEGY
We're assuming a brute-force guessing strategy. A guesser needs to guess all possible passwords 
up to and including the given length to ensure they find the matching one

'''

def get_num_guesses(length):
    total = 0

    for x in range(length):
        total += 26 ** (x+1)
    return total
            
'''
When ** is used between two numbers, it serves as the exponentiation operator, 
indicating that the number on the left should be raised to the power of the number 
on the right. 
'''