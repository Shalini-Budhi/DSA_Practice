# Insertion Sort

# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: The sorted array will be [1, 3, 4, 7, 9].
# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Input: arr[] = [4, 1, 9]
# Output: [1, 4, 9]
# Explanation: The sorted array will be [1, 4, 9].

def insertionSort(arr):

  for i in range(0,len(arr)-1):
    for j in range(i+1,0,-1):
      if(arr[j]<arr[j-1]):
        arr[j],arr[j-1] = arr[j-1],arr[j]
      else:
        break
  return arr


arr = [4, 1, 3, 9, 7]
print(insertionSort(arr))

# The first for loop starts from index 0.
# for i in range(0, len(arr) - 1):
# The second for loop starts from i + 1 and moves backwards.
# for j in range(i + 1, 0, -1):
# Compare the current element with the previous element.
# if arr[j] < arr[j - 1]:
# If the current element is smaller than the previous element, swap their values.
# arr[j], arr[j - 1] = arr[j - 1], arr[j]
# After swapping, the loop continues moving backwards and compares the element again with the previous element.
# If the current element is greater than or equal to the previous element, the elements are already in the correct order.
# In that case, we use break to stop the inner loop.
# else:
#     break
# After the inner loop finishes, the outer i loop moves to the next element and repeats the same process.