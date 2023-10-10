'''
ASSIGNMENT

Complete the power_set function using the following algorithm:

1. Check if the input list is empty. If it is, return a list containing an empty list.
(The power set of an empty set is a set containing just the empty set)

2. Otherwise, create an empty list to hold all the final subsets of the input list.

3. Recursively call power_set. Pass in all of the elements in the input set except the first one.

4. Iterate over the list of subsets returned from the recursive call. For each subset, append two 
new subsets to the final list of subsets:

first_item_from_input_set + subset
subset

5. Return the list of subsets

'''

def power_set(input_set):
    if not input_set:
        return [[]]

    first = input_set[0]
    rest = input_set[1:]
    
    # Recursively generate the power set of the remaining elements.
    recurse = power_set(rest)

     # Create a list of all the subsets that include the first element.
    subsets = []
    for x in recurse:
        subsets.append([first] + x)


    # Create a list of all the subsets that do not include the first element.
    for y in recurse:
        subsets.append(y)

    return subsets