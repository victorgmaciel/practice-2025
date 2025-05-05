# Remove Duplicates From Sorted Array
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.
#
# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.
#
# Note:
#
# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.
from typing import List


nums_test_case_one=[2,10,10,30,30,30]

def remove_duplicates(nums: List[int]) -> int:

    # always a unique value at index 0, so the next unique should
    # go at index 1
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l










print(remove_duplicates(nums_test_case_one))