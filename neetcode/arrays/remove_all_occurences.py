# Given:
# A list of sorted integers nums and an integer target.
#
# Task:
# Remove all occurrences of target from the list in-place (without using extra space).
# Return the new length of the list after removals.
#
# You must modify the list in-place such that the first new_length elements of nums contain all elements except the target, and the order of elements should be preserved.
from typing import List

nums_test = [2, 3, 3, 5, 6, 6, 6, 7]

target_test = 6
#
# Output: 5
# Modified nums (first 5 elements): [2, 3, 3, 5, 7, _, _, _]

def remove_target( nums: List[int], target: int) -> tuple[int, any]:
    left = 0 # track where the next non-target number should go

    for i in range(len(nums)):
        if nums[i] != target:
            nums[left] = nums[i]
            left += 1

    return left
print(remove_target(nums_test, target_test))