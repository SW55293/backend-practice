'''
ASSIGNMENT
In Socialytics, now we need to display to our users the people who follow 
them with the highest follower count. This will help them know which of their 
followers they should follow back.

Complete the find_max function. It should take a list of integers and return the 
largest value in the list.

The "runtime complexity" (aka Big O) of this function should be O(n)
'''





def find_max(nums):
    big = float("-inf")

    for x in nums:
        if x > big:
            big = x
    return big