# Find Sum of AP Series


# 0

# Problem Statement: Given an A.P. Series, we need to find the sum of the Series.

# Examples
# Example 1:
# Input:
#   n = 4, a = 2, d = 2  
# Output:
#  20  
# Explanation:
#   The series is 2, 4, 6, 8.  
# The sum of the series is 2 + 4 + 6 + 8 = 20.

# Example 2:
# Input:
#   n = 8, a = 2, d = 5  
# Output:
#  124  
# Explanation:
#  The series is 2, 7, 12, 17, 22, 27, 32, 37.  
# The sum of the series is 2 + 7 + 12 + 17 + 22 + 27 + 32 + 37 = 156.

def sum_Of_Ap(n,a,d):
  sum = 0
  for i in range(n):
    sum += a
    a += d
  return sum

n, a, d = map(int, input().split())

print(sum_Of_Ap(n,a,d))

