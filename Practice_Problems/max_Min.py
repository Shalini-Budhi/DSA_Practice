# Maximum and Minimum Digit in a Number

# Problem Statement: Given a number N, print the smallest and largest digits present in the number.

# Examples
# Input: N = 2746
# Output: Largest digit: 7, Smallest digit: 2
# Explanation: 
# Largest digit in N is 7 whereras smallest digit is 2.
# Input: N = 23004
# Output: Largest digit : 4, Smallest digit : 0
# Explanation: 
# Largest digit in N is 4 whereras smallest digit is 0.


def max_min(n):
  max_digit = 0
  min_digit = 9
  digit = 0
  while n>0:
    digit = n %10
    if n > max_digit:
      max_digit = digit
    if n < min_digit:
      min_digit = digit
    n = n//10
  return max_digit,min_digit
n = int(input())
print(max_min(n))


