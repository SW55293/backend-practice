'''
ASSIGNMENT
Complete the reverse_string function.

It should take a string as a parameter and return the reversed string by recursively reversing 
the substrings inside. Your function should recurse once for each character in the string.
'''

def reverse_string(s):
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]
