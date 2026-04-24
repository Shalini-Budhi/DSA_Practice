# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

# A palindrome is a number that reads the same backward as forward. For example, 121, 1331, 
# and 4554 are palindromes because they remain the same when their digits are reversed.

# Examples
# Example 1:
# Input:N = 4554
# Output:Palindrome Number
# Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
                                        
# Example 2:
# Input:N = 7789          
# Output: Not Palindrome
# Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome


def palindrome_number(n):
  s = str(n)
  left = 0
  right = len(n) - 1
  while left < right:
    if n[left] != n[right]:
     return False
    left += 1
    right -= 1
  return True
n = (input())
if(palindrome_number(n)):
  print("Palindrome Number")
else:
  print("Not Palindrome Number")


# def palindrome_number(n):
#   original_number = n
#   reverse = 0
#   while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n //10
#   return original_number == reverse
# n = int(input())
# if palindrome_number(n):
#   print("Palindrome Number")
# else:
#   print("Not Palindrome Number")

