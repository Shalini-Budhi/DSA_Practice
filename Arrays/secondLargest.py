# // Find Second Smallest and Second Largest Element in an array


# // 43

# // Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# // Examples
# // Example 1:
# // Input:
# //  [1, 2, 4, 7, 7, 5]  
# // Output:
  
# // Second Smallest : 2  
# // Second Largest : 5  
# // Explanation:
# //   The elements are sorted as 1, 2, 4, 5, 7, 7.  

import math
def second_Smallest_Elelments(arr):
  smallest = arr[0]
  second_Smallest = math.inf

  largest = arr[0]
  second_Largest = -math.inf

  for i in range (len(arr)):
    #second Smallest
     if arr[i] < smallest:
            second_Smallest = smallest
            smallest = arr[i]
     elif arr[i] > smallest and arr[i] < second_Smallest:
            second_Smallest = arr[i]
    #second Largest
     if arr[i] > largest:
          second_Largest = largest
          largest = arr[i]
     elif arr[i] < largest and arr[i] > second_Largest:
          second_Largest =arr[i]
  return smallest,second_Smallest,largest,second_Largest

arr = list(map(int, input().split()))
print(second_Smallest_Elelments(arr))