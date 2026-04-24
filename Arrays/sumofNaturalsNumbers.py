# Sum of first N Natural Numbers

# 9

# Problem Statement: Given a number N find out the sum of the first N natural numbers .

# Examples
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

def natural_Number(n):
  sum = 0
  for i in range(1,n+1):
    sum =sum+i
  return sum
n = int(input())
print(natural_Number(n))