# Find All Numbers Disappered in an array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

def disapperedNumbers(arr):

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
      result.append(i+1)

  return result

arr = [4,3,2,7,8,2,3,1]
print(disapperedNumbers(arr))


# Problem explanation

# First, sort the array using Cyclic Sort.

# After sorting, use a for loop to check each index.
  
# At each index, check the condition arr[i] != i + 1.

# If the condition is true, i + 1 is a missing number.

# Append the missing number to the result array using result.append(i + 1).

# Finally, return the result array.