'''
Assignment

For each index:
Set smallest_idx to the current index
For each index from smallest_idx+1 to the end of the list:
If the number at the inner index is smaller than the number at smallest_idx, set smallest_idx to the inner index
Swap the number at the current index with the number at smallest_idx
'''

def selection_sort(nums):
    for x in range(len(nums)):
        smallest_idx = x
        for y in range(x+1, len(nums)):
            if nums[y] < nums[smallest_idx]:
                smallest_idx = y
        nums[smallest_idx], nums[x] = nums[x], nums[smallest_idx]
    return nums
