'''
ASSIGNMENT
In the social media industry, there is a concept called "spread" - it refers 
to how much a post spreads due to "reshares" after all of the original author's 
followers see it. Complete the get_estimated_spread function. The only input is 
audiences_followers, which is a list of the follower counts of all the followers of the author.

estimated_spread = average_audience_followers * ( num_followers^1.2 )

In the formula above, average_audience_followers refers to an average calculated from each
number within the audiences_followers argument - which is a list containing the user's follower's
individual follower count.

For example, if audiences_followers = [2, 4, 2, 19], then the influencer has 4 followers, 
and each of them has their own follower counts of 2, 4, 2, and 19 respectively.
'''

# My try
def get_estimated_spread(audiences_followers):
    
    num_followers = len(audiences_followers)
    average_audience_followers = sum(audiences_followers) /len(audiences_followers)
    estimated_spread = average_audience_followers * ( num_followers**1.2 )

    return estimated_spread

# the solution given
def get_estimated_spread(audiences_followers):
    sum = 0
    for num in audiences_followers:
        sum += num

    num_followers = len(audiences_followers)
    average_audience_followers = sum / num_followers
    return average_audience_followers * (num_followers**1.2)


# don't touch below this line


def test(nums):
    res = round(get_estimated_spread(nums))
    print(f"Follower counts: {nums}")
    print(f"Estimated spread: {res}")
    print("====================================")


def main():
    test([7, 4, 3, 100, 765, 2344, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])


main()
