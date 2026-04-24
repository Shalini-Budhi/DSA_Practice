# Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

# Note: A palindromic number is a number that remains the same when its digits are reversed. 
# OR & a palindrome is a number that reads the same forward and backward Eg: 121,1221, 2552

# Examples

# Example 1: 
# Input: min = 10 , max = 50 
# Output: 11 22 33 44  
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward. 

# Example 2: 
# Input: min = 100 , max = 150 
# Output: 101 111 121 131 141  
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward. 


def is_palidrome(n):
  original_num = n
  reverse = 0
  while n>0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
  return original_num == reverse
def palindome_Check(min,max):
  count = 0
  for i in range(min,max+1):
    if is_palidrome(i):
      count +=1
      print(i,end=" ")
min = int(input())
max = int(input())
palindome_Check(min,max)
