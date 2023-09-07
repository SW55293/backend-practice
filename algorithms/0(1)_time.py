'''
ASSIGNMENT
We need to be able to search our Socialytics user base more quickly! Our users are complaining 
that the search bar is painfully slow. You'll notice that if you run the code in its current state, 
it will take a very long time.

The find_last_name function takes "names_dict", a dictionary of first_name -> last_name. 
It also accepts a first_name. If first_name is a key in the dictionary, find_last_name returns 
the associated last name. If the key is not found, it returns None. Make sure you handle the case 
where the first_name is not in the dictionary!

Write the function so that it runs quickly! It should be O(1).



'''


def find_last_name(names_dict, first_name):
    # for x in names_dict:
    #     if x == first_name:
    #         return list(names_dict.keys()).index(x)
    # return None
    return names_dict.get(first_name)



'''
To make the function O(1), we can use a dictionary lookup. A dictionary lookup is a very efficient 
operation, and it takes O(1) time.

This function works by first checking if the first_name key is in the dictionary. If it is, 
the function returns the associated value. Otherwise, the function returns None.

The get() method of a dictionary is a dictionary lookup. It takes O(1) time to execute, 
regardless of the size of the dictionary.

So, the updated find_last_name function is O(1).
'''