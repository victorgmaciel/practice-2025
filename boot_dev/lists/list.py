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




