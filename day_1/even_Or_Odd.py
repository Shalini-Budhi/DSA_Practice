# 2. Determine Even or Odd
# Problem
# Write a program that takes an integer as input and determines whether the number is even or odd.
# Input
# number
# Constraints
# - 1 ≤ number ≤ 10000
# Example
# Input: 8
# Output: Even Number
# Input: 7
# Output: Odd Number


def evenOROdd(n):
  if n%2==0:
    print("Even Number")
  else:
    print("Odd number")
n = int(input())
evenOROdd(n)