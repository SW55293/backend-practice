'''
ASSIGNMENT
Complete the get_common_formats function. It should take in two arguments, formats1 and formats2, each a list of 
strings representing the file formats supported by two different pieces of software.

It should return a set of strings representing the file formats that are supported by both pieces of software.
'''

# Convert to sets first

def get_common_formats(formats1, formats2):
    set1 = set(formats1)
    set2 = set(formats2)
    formats3 = set1.intersection(set2)
    return formats3
