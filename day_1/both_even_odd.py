# 9. Check Both Numbers Even, Odd, or Mixed
# Problem
# Write a program that takes two numbers and determines whether both numbers are even, both are odd, or one is even and the other is odd.
# Input
# a, b
# Constraints
# - 1 ≤ a, b ≤ 10000
# Example
# Input:
# a = 4
# b = 8
# Output:
# Both Even

def bothNumEvenOdd(a,b):
  if (a%2 == 0 and b%2 == 0):
    print("Both Even")
  elif (a%2 != 0 and b%2 != 0):
    print("Both Odd")
  else:
    print("Mixed Numbers")
a = int(input())
b = int(input())
bothNumEvenOdd(a,b)