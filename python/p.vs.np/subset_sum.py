'''
ASSIGNMENT
Complete the subset_sum function.

It should take a list of integers nums and an integer target, and return True if there exists a subset of nums that adds up to target, and False otherwise.

PSEUDOCODE: SUBSET_SUM(NUMS, TARGET)
INPUTS
nums: A list of integers representing the follower counts of influencers.
target: The target sum we want to find a subset for.
OUTPUT
True if there exists a subset of nums that adds up to target. False otherwise.

ALGORITHM
Call the helper function starting with the last index in nums and return its result.
PSEUDOCODE: FIND_SUBSET_SUM(NUMS, TARGET, INDEX)
INPUTS
nums: A list of integers representing the follower counts of influencers.
target: The target sum we want to find a subset for.
index: The index of the current element we're considering.
OUTPUT
True if there exists a subset of nums that adds up to target. False otherwise.

ALGORITHM
If the target is 0, return True.
If the index less than 0 and the target is not 0, return False.
If the number at the current index is greater than the target, call the helper function with the same target but with the index decremented by 1, and return the result, we're done.
Otherwise, call the helper function with the same target and index decremented by 1, and save the result.
Also, call the helper function with the target reduced by the value of the current element and the index decremented by 1
If either of these calls returns True, return True. Otherwise, return False.

'''


def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums)-1)


def find_subset_sum(nums, target, index):
    if target == 0: return True

    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        return find_subset_sum(nums, target, index - 1) or find_subset_sum(nums,target - nums[index], index - 1)