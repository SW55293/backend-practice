'''
ASSIGNMENT
Socialytics needs a new tool that allows big brands to see how many of an influencer's 
followers are loyal to their brand. Complete the get_avg_brand_followers function. 
It takes two inputs:

all_handles: a 2-dimensional list, or "list of lists" of strings representing instagram 
user handles on a per-influencer basis.

brand_name: a string.

get_avg_brand_followers returns the average number of handles that contain the brand_name 
across all the lists. Each list represents the audience of a single influencer.
'''

def get_avg_brand_followers(all_handles, brand_name):
    counter = 0

    for row in all_handles:
        for item in row:
            if brand_name in item:
                counter += 1
    return counter / len(all_handles) 
