'''
ASSIGNMENT
Complete the remove_duplicates function.

It should iterate over all the follower counts in the nums and remove all 
the duplicate numbers, then return the list of unique follower counts.

We want to preserve the order of the list. Dont use a set


'''

def remove_duplicates(nums):
    new_list = []
    for x in nums:
        if x not in new_list:
          new_list.append(x)

    return new_list