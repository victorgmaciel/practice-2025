"""
get estimated spread of post
"""

# estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

# average_audience_followers is an average calculated from each number within the audience followers, list containing
# the individual follower counts of the author's followers.
# ex: audience_followers = [2,3,2,19]
# so 4 total followers
# each follower has their own

# Inputs: [10, 200, 3000, 5000, 4]
# Expecting: 11333
def get_estimated_spread(audiences_followers):

    if not audiences_followers:
        return 0

    # number of followers
    count_of_followers = len(audiences_followers)
    # get average
    num_for_average = 0
    for followers in audiences_followers:
        num_for_average += followers
    estimated_spread = (num_for_average / count_of_followers) * (count_of_followers ** 1.2)
    return estimated_spread






first_try = ([10, 200, 3000, 5000, 4])

get_estimated_spread(first_try)



