from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Note this is for a 1 index array
    :param numbers: list of numbers
    :param target: target desired
    :return: indices of two numbers that result in sum
    """

    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        current_sum = numbers[left_pointer] + numbers[right_pointer]
        if current_sum == target:
            return left_pointer + 1, right_pointer + 1

        if current_sum < target:
            left_pointer += 1

        else:
            right_pointer -= 1




numbers_1 = [2, 7, 11, 15]
target_1 = 9
print(two_sum(numbers_1, target_1))
