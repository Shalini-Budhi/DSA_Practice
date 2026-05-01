# Program to find Sum of GP Series


# 0

# Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as
# 1. a, first term
# 2. r, common ratio
# 3. n, number of terms
# Write a program to find the sum of the Geometric Progression Series.

# Examples
# Input: a=1 , r=0.5 , n=3
# Output: 1.75 
# Explanation: The elements of GP are 1, 0.5 and 0.25
# Input: a=3 , r=5 , n=2
# Output: 18.
# Explanation: The elements of GP are 3 and 15

def sum_Of_Gp(a,r,n):
  sum = 0
  for i in range(n):
    sum += a
    a *= r
  return sum
a, r, n = input().split()

a = float(a)
r = float(r)
n = int(n)

print(sum_Of_Gp(a,r,n))