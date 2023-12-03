'''
Assignment:

Procedure bubble_sort(nums):
    Set swapping to True
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to the last element:
            If the (i-1)th element of nums is greater than the ith element:
                Swap the (i-1)th element and the ith element of nums
                Set swapping to True
    Return nums
End Procedure

'''

def bubble_sort(nums):
    swapping = True

    while swapping:
        swapping = False
        for x in range(len(nums[1:])):
            if nums[x] > nums[x + 1]:
                nums[x], nums[x + 1] = nums[x + 1], nums[x]
                swapping = True

    return nums