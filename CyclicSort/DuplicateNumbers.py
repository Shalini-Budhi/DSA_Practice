# 2.Find the Duplicate Numbers

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3


def duplicateNumbers(arr):
   i = 0
   while i < len(arr):
      current_index = arr[i] - 1
      if arr[i] != arr[current_index]:
         arr[i],arr[current_index] = arr[current_index],arr[i]
      else:
         if i != current_index:
            return arr[i]
         i += 1

   return arr
        

arr =[1,3,4,2,2]
print(duplicateNumbers(arr))


# Problem Explanation

# First, check whether the current element is at its correct index position.

# If the element is not in its correct position, swap it with the element at its correct index.

# If the element is already in its correct position, no swap is needed.

# Then check whether the correct index already contains the same element.

# If i != current_index, it means the same element already exists at its correct position, so we have found a duplicate.

# Return arr[i] as the duplicate element.

# If there is no duplicate at the current position, increment i and continue checking the next element.