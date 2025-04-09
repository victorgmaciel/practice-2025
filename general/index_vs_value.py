"""general knowledge"""


# In an array or list in python, list is the position of an element
# value is the data stored at that position

arr = ['a', 'b', 'c']

# index here is 0,1,2

# value here is 'a', 'b', 'c'

# so
print(arr[0]) # returns the value at index 0
# saying give me the value at this index

# now looping

# loop over values
for value in arr:
    print(value)


# loop over index
for i in range(len(arr)):
    print(i, 'here is value', arr[i])

# getting both
for i, value in enumerate(arr):
    print(i, value)

# remember
# arr[x] asking for value at index x
# in you loop like for x inn arr: x is the value not the index.