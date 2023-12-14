'''
INSTRUCTIONS FOR WRITING THE FUNCTION
If either keys or values length is empty return an empty dictionary
Get the result of recursively calling zipmap on all but the first element from keys and values
Add the first element of keys as a property on the resulting dictionary, and set its value to the first element in values
Return the new resulting dictionary
You'll note that by structuring the recursive function this way, the resulting dictionary should present its entries in reverse order 
based on the given lists. Just like the example above.

'''

def zipmap(keys, values):

    # Base case: If either keys or values length is empty, return an empty dictionary
    if not keys or not values:
        return {}

    # Recursive case: Get the result of recursively calling zipmap on 
    # all but the first element from keys and values
    result = zipmap(keys[1:],values[1:])
    
    # Add the first element of keys as a property on the resulting dictionary,
    # and set its value to the first element in values
    result[keys[0]] = values[0]

    return result
