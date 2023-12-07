'''
MEMOIZATION IS JUST CACHING

At its core, memoization is just a specific type of caching. It's when we cache (store a copy of) 
the result of a computation so that we don't have to compute it again in the future.
'''

'''
ASSIGNMENT
Sometimes Doc2Doc needs to calculate the number of words in a piece of text. 
This can be a slow operation, so we want to memoize it.

Complete the word_count_memo function. It takes a document (string) and a dictionary of document -> word 
count pairs called memos. It should return two values, the word count of the document and an updated memos dictionary.

Make sure you are using memoization, if the result for a given document is already in the memos dictionary, 
it should return the result instead of computing it again. If there is no existing result in the memos dictionary, 
we should compute the word count and update the memos dictionary with the new result added.

You can use the pure word_count function that I wrote for you in your solution.


'''

def word_count_memo(document, memos):

    memos_copy = memos.copy()
    
    if document in memos_copy:
        return memos_copy[document], memos_copy
        
    count = word_count(document)
    memos_copy[document] = count
    return count, memos_copy


def word_count(document):
    count = len(document.split())
    return count


'''
IS IT ALWAYS GOOD TO MEMOIZE?
Nope! Memoization is a tradeoff. It's a tradeoff between memory and speed. If you have a function that's called often, 
but it's not very expensive to compute, then it's probably not worth memoizing because you'll be bloating the amount of 
RAM your program uses storing the results of the function.

It's also a decent amount of extra code to write, so you should only do it if you have a good reason to.


'''