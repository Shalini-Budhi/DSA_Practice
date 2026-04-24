# Check whether a given number is even or odd


# 0

# Problem Statement: Given a number n, check whether a given number is even or odd.

# Examples

# Input: n=5
# Output: odd
# Explanation: 5 is not divisible by 2.

# Input: n=6
# Output: even
# Explanation: 6 is divisible by 2.

def even_Odd(n):
  if n % 2 != 0:
    print("Odd")
  else:
    print("Even")
n = int(input())
even_Odd(n)