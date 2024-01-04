'''
ASSIGNMENT
Keeping track of how many words are in collections of documents is a key function of Doc2Doc.

Complete the word_count_aggregator function. It should return a function that calculates the 
number of words in its input (doc, a string). It should then add that number to an enclosed 
count value and return the new count. In other words, it keeps a running total of the count variable within a closure.

TIP
I used .split() to count the number of words in the doc string.
'''

def word_count_aggregator():
    count = 0
    def calc_words(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return calc_words
        
