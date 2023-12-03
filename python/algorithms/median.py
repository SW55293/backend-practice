'''
ASSIGNMENT
Complete the median_followers() function to find the median 
follower count of the given list of numbers.
Order matters - You'll probably want to use the sorted() method to help you out.
'''
from statistics import median

def median_followers(nums):
    # nums.sort()
    return median(nums)
'''
nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    return nums[n // 2]
'''


# don't touch below this line


def test(nums):
    res = round(median_followers(nums))
    print(f"Follower counts: {nums}")
    print(f"Median follower count: {res}")
    print("----")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])
    test([10, 200, 3000, 5000, 4, 6])


main()
