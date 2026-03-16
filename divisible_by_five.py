# 3. Check Divisibility by 5
# Problem
# Write a program that checks whether a given number is divisible by 5.
# Input
# number
# Constraints
# - 1 ≤ number ≤ 10000
# Example
# Input: 20
# Output: Divisible by 5
# Input: 17
# Output: Not Divisible by 5


def divisibleByFive(n):
  if n%5 == 0:
    print(" Number Divisible by 5")
  else:
    print("Number is not divisible by 5")
n = int(input())
divisibleByFive(n)