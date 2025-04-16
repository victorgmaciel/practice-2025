"""
LockedIn needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their brand.
 Complete the get_avg_brand_followers function. It takes two inputs:

all_handles: a 2-dimensional list, or "list of lists" of strings representing user handles on a per-influencer basis.
brand_name: a string.
get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each
 list represents the audience of a single influencer.

Example Input/Output
Input:

all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"

Expected output: 1.33 (handles per influencer, because 4 handles contained "cosmo" and there are 3 lists)
"""
from os.path import split

all_handles_test = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name_test = "cosmo"

def get_avg_brand_followers(all_handles, brand_name):

    # length of the list of lists
    count_of_lists = len(all_handles)

    # iterate through all_handles
    counter_result = 0
    for handles in all_handles:
        for individual_handles in handles:
            if individual_handles.startswith(brand_name):
                counter_result += 1
    return counter_result / count_of_lists







get_avg_brand_followers(all_handles_test, brand_name_test)
