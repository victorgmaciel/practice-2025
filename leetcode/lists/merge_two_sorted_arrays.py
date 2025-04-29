"""
Here is a common problem for practices two pointers.
Let's say we have two sorted arrays
arr_one = [1,3,7,10,15]
arr_two = [2,4,6,9,13]

goal here is to merge the two arrays into one, ensuring that they stay stored
"""


def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0

    # compare the two values of sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # in the case that the arrays are done comparing and there is still more values
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


arr_one = [1, 3, 7, 10, 15]
arr_two = [2, 4, 6, 9, 13]

print(combine(arr_one, arr_two))
