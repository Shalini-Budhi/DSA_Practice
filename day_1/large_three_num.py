# 6. Find the Largest of Three Numbers
# Problem
# Write a program that takes three numbers as input and determines the largest number among them.
# Input
# a, b, c
# Constraints
# - 1 ≤ a, b, c ≤ 10000
# Example
# Input:
# 10, 25, 15
# Output:
# 25 is the largest

def large_three_num(a,b,c):
  if a>b and a>c:
    print("A is Large")
  elif b>a and b>c:
    print("B is Large")
  else:
    print("C is Large")
a = int(input())
b = int(input())
c = int(input())
large_three_num(a,b,c)