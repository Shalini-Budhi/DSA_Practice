# Problem Statement: Given an array, we have found the number of occurrences of each element in the array.

# Examples
# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	            5  2
#                 15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array

# Example2: 
# Input: arr[] = {2,2,3,4,4,2};
# Output: 2  3
# 	           3  1
#                4  2
# Explanation: 2 occurs 3 times in the array
# 	     3 occurs 1 time in the array
#              4 occurs 2 time in the array


def count_frequency(arr,n):
  count = 0 
  found = [False]*n

  for i in range(n):
    if found[i]:
      continue
    count = 1
    for j in range(i+1,n):
      if arr[i] == arr[j]:
        found[j] = True
        count += 1
  return count

arr= list(map(int,input().split()))
n = int(input())
print(count_frequency(arr,n))  