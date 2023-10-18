# lists are mutable, can be changed
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# [1, 2, 3, 4]

# tuples are immutable, cannot be changed
my_tuple = (1, 2, 3)
my_new_tuple = my_tuple + (4,)
print(my_new_tuple)
# (1, 2, 3, 4)


'''
ASSIGNMENT
There's a bug on line 4 in the add_doc function! Whoever wrote it assumed that 
documents was a list, but it's actually a tuple.

Run the code to see the error.

Fix the bug by creating a new tuple with the new_doc added to the end and returning that.
'''

def add_doc(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents
