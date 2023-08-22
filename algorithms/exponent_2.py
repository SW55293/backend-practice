'''
ASSIGNMENT
While the influencers who use our platform are really great at taking selfies, 
most aren't super great at math. We need to write a tool that predicts an influencer's 
follower growth over time.

Complete the get_follower_prediction function.

"fitness" influencers have their follower count quadruple each month
"cosmetic" influencers have their follower count triple each month
All other influencers have their follower count double each month
For example, if a fitness influencer starts with 10 followers, then after 1 
month they should have 40 followers. After 2 months, they would have 160 followers. etc.

EXTRA CREDIT
Try to avoid using a loop by using a slightly modified geometric sequence formula instead.

total = a1 * r^n
'''
# My Try
def get_follower_prediction(follower_count, influencer_type, num_months):


    if influencer_type == "fitness":
        exp = 4
    elif influencer_type == "cosmetic":
        exp = 3
    else:
        exp = 2
    total = follower_count * (exp ** num_months)
    return total


# Given Solution
def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        return follower_count * (4**num_months)
    if influencer_type == "cosmetic":
        return follower_count * (3**num_months)
    return follower_count * (2**num_months)

# don't touch below this line


def test(follower_count, influencer_type, num_months):
    predicted = get_follower_prediction(follower_count, influencer_type, num_months)
    print(f"- Follower count: {follower_count}")
    print(f"- Type: {influencer_type}")
    print(f"- Months: {num_months}")
    print(f"Prediction: {predicted}")
    print("====================================")


def main():
    test(10, "fitness", 1)
    test(10, "fitness", 2)
    test(10, "fitness", 4)
    test(12, "cosmetic", 4)
    test(15, "business", 4)
    test(10, "fitness", 5)
    test(10, "fitness", 6)
    test(10, "fitness", 7)
    test(10, "fitness", 8)
    test(10, "fitness", 9)


main()
