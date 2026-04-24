# Problem Statement: Given two integers a and b, find prime numbers in a given range [a,b], 
# (a and b are included here).

# Examples
# Input: a = 2, b = 10
# Output: [2, 3, 5, 7]  
# Explanation: Prime Numbers between 2 and 10 are 2,3,5 and 7.
# Input: a = 10, b = 16
# Output: [11, 13] 
# Explanation: Prime Numbers between 10 and 16 are 11 and 13.

def is_palindrome(n):
  if n <= 1:
    return False
  
  for i in range (2,n):
    if n % i == 0:
      return False
  return True

def palindrome_count(min,max):
  count = 0
  for j in range(min,max+1):
    if is_palindrome(j):
      count += 1
      print(j,end=" ")
min = int(input())
max = int(input())
palindrome_count(min,max)
