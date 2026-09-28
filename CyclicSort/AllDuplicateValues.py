# 3. Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []



def allDuplicateValues(arr):

  i = 0

  while i < len(arr):
     current_index = arr[i] - 1
     if arr[i] != arr[current_index]:
        arr[i],arr[current_index] = arr[current_index],arr[i]
     else:
        i += 1

  result = []

  for i in range(0,len(arr)):
     if arr[i] != i+1:
        result.append(arr[i])
  return result

arr = [4,3,2,7,8,2,3,1]
print(allDuplicateValues(arr))


# First, initialize i = 0 to start checking the array from the first index.

# Use a while loop to traverse the array:

# while i < len(arr):

# Find the correct index of the current element:

# current_index = arr[i] - 1

# Because the numbers are from 1 to n, the correct index is number - 1.

# Check whether the current element is in its correct position:

# if arr[i] != arr[current_index]:

# If it is not in the correct position, swap the elements:

# arr[i], arr[current_index] = arr[current_index], arr[i]
# After swapping, don't increase i immediately.
# We check the same index again because a new element has been placed there.

# If the current element is already in the correct position, move to the next index:

# else:
#     i += 1

# After the cyclic sort is completed, create an empty result array:

# result = []

# Use a for loop to check every index:

# for i in range(len(arr)):

# Compare the actual value with the expected value:

# if arr[i] != i + 1:
# If they are different, the current value is a duplicate because i + 1 should be at that index.

# Add the duplicate value to the result array:

# result.append(arr[i])

# Finally, return the result array:

# return result

