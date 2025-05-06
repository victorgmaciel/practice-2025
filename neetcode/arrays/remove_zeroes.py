"""
Move Zeroes
Given:
An array of integers nums.

Task:
Move all the zeroes to the end of the array in-place, while maintaining the relative order of the non-zero elements.

Return is not needed — just modify the list in-place.
"""

# Input:  nums = [0, 1, 0, 3, 12]
# Output: nums becomes [1, 3, 12, 0, 0]
from typing import List

nums_test = [0, 1, 0, 3, 12]


def move_zeros(nums: List[int]) -> None:
    l = 0
    for r in range(len(nums)):  # start at 0
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
    for i in range(l, len(nums)):
        nums[i] = 0








print(move_zeros(nums_test))
print(nums_test)
