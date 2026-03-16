# Problem
# Write a program that takes two numbers as input and determines which number is larger.
# Input
# a, b
# Constraints
# - 1 ≤ a, b ≤ 10000
# Example

# Input:
# a = 10
# b = 20
# Output:
# 20 is larger

def largetwoNumber(a,b):
  if a>b:
    print("a is large")
  elif a<b:
    print("b is large")
a = int(input())
b = int(input())
largetwoNumber(a,b)