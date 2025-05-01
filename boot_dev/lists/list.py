"""
Python list practice
"""

# get values above certain threshold

nums = [1,2,3,5,6,10,11,20,100]
nums_above_three = []

for num in nums:
    if num >= 3:
        nums_above_three.append(num)
print(nums_above_three)

# list comprehension
new_nums = [num for num in nums if num >= 3]
print(new_nums)

# List basics

this_is_a_list = ["iron born", "sea lady", "titanic"]

# Sometime lists can be declared as for readability
flower_types = [
    "rose",
    "chrysanthemum",
    "daffodil"
]

# start counting at 0
# index is 0, 1, 2, 3
names = ["Bob", "lane", "Alice", "Breanna"]

# can get items via index
print(names[1])

#The length of the list is equal to the number of items present.
# Don't be fooled by the fact that the length is not equal to the
# index of the last element, in fact, it will always be one greater.
print(len(names)) # gives value length
print(len(names) - 1) # gives index length

# List updates
# we can update lists as follows
names[0] = "Victor"
print(names)

# we can append items to the end of lists
names.append("Bob")
print(names)

# Pop is the opposite of append, it will remove the last item of the list
name_removed = names.pop()

print(name_removed) # this will be Bob

# iterate over items in a list
sports = ["basketball", "baseball", "football", "soccer", "swimming"]

for i in range(0, len(sports)):
    print(sports[i])


# a function where we compare character levels
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)

# this just accesses through index
check_character_levels()

# let's say lists are not the same len
# prevent an indexError by
# min(len(old_character_levels), len(new_character_levels)) getting the smaller of the lists



# Modulo operations

# Finding odd numbers
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers

# Other ways to find odd numbers
# if i % 2 != 0:  # remainder when divided by 2 is not 0
# if i & 1:  # The least significant bit is 1 for odd numbers
# if i / 2 != i // 2:  # True division vs floor division
# if not (i % 2 == 0):  # Negation of even check
# if i % 2 == 1:  # remainder when divided by 2 is exactly 1



# SLICING LISTS


scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

# using just the step section
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

#negative indices
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]


# LIST OPERATIONS CONCATENATE

# just use + operator
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]

# contains
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

# List Deletion
# Python has a built-in keyword del that deletes items from objects.
# In the case of a list, you can delete specific indexes or entire slices.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []