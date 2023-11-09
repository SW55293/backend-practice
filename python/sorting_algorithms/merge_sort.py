'''
Assignment

MERGE_SORT() IMPLEMENTATION
Input: A, a list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Call merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
MERGE() IMPLEMENTATION
Inputs: A, B. Two lists of integers

Create a new "final" list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer than the other). Add those extra items to the final list.
Return the final list.

'''

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    first_half = nums[:mid]
    second_half = nums[mid:]
    f = merge_sort(first_half)
    s = merge_sort(second_half)

    return merge(f, s)
    

def merge(first, second):
    if not first: return second

    if not second: return first

    final_list = []
    i = 0
    j = 0
    
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
          final_list.append(first[i])
          i += 1
        else:
          final_list.append(second[j])
          j += 1

    # Add any remaining elements from the first list.
    while i < len(first):
        final_list.append(first[i])
        i += 1

    # Add any remaining elements from the second list.
    while j < len(second):
        final_list.append(second[j])
        j += 1

    return final_list