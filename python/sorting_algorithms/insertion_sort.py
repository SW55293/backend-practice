def insertion_sort(nums):
    #For each index in the input list:
    for x in range(1, len(nums)):
        #Set a j variable to the current index
        j = x
        #While j is greater than 0 and the element at index j-1 is greater than the element at index j:
        while (j > 0) and (nums[j] < nums[j -1]):
            #Swap the elements at indices j and j-1
            nums[j], nums[j-1] = nums[j -1], nums[j]
            #Decrement j by 1
            j -= 1
    return nums