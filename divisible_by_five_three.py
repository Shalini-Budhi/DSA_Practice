# 4. Check Divisibility by 3 and 5
# Problem
# Write a program to determine whether a given number is divisible by 3, 5, both, or neither.
# Input
# number
# Constraints
# - 1 ≤ number ≤ 10000
# Example
# Input: 15
# Output: Divisible by 3 and 5


def divisible_Five_Three(n):
  if (n%5 == 0 and n%3 == 0):
    print("Number id divisible both 3&5")
  else:
    print("Number is not divisible")
n = int(input())
divisible_Five_Three(n)