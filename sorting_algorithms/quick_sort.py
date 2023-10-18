'''
PSEUDOCODE: QUICK_SORT(NUMS, LOW, HIGH)
If low is less than high:
Partition the input list using the partition function
Recursively call quick_sort on the left side of the partition
Recursively call quick_sort on the right side of the partition
Return the list

PSEUDOCODE: PARTITION(NUMS, LOW, HIGH)
Set pivot to the element at index high
Set i to low
For each index (j) from low to high
If the element at index j is less than the pivot:
Swap the element at index i with the element at index j
Increment i by 1
Swap the element at index i with the element at index high
Return the list and the index i


'''

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums,low, p - 1)
        quick_sort(nums, p + 1, high)

    return nums
    

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low,high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return nums and i 
