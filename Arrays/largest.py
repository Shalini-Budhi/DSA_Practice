# Find the Largest element in an array

# Problem Statement: Given an array, we have to find the largest element in the array.

# Examples
# Example 1:
# Input:
#  arr[] = {2, 5, 1, 3, 0}  
# Output:
#  5  


def largest_Element(arr):
  largest = arr[0]
  for i in range(0,len(arr)):
    if arr[i] > largest:
      largest = arr[i]
  return largest
arr = list(map(int, input().split()))
print(largest_Element(arr))