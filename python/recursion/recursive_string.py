'''
ASSIGNMENT
Complete the reverse_string function.

It should take a string as a parameter and return the reversed string by recursively reversing 
the substrings inside. Your function should recurse once for each character in the string.
'''

def reverse_string(s):
    # base case
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]

# Example

# Original String: "Hello"

# Recursive Step 1:
# reverse_string("ello") + "H"
#   Recursive Step 2:
#   reverse_string("llo") + "e"
#     Recursive Step 3:
#     reverse_string("lo") + "l"
#       Recursive Step 4:
#       reverse_string("o") + "l"
#         Base Case: "o"
#       Result: "o" + "l" = "ol"
#     Result: "ol" + "l" = "oll"
#   Result: "oll" + "e" = "olle"
# Result: "olle" + "H" = "olleH"

# Final Reversed String: "olleH"
