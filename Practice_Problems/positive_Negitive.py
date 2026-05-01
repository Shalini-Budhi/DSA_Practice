# Check whether a number is positive or negative


# 0

# Problem Statement: Given a number n check whether it's positive or negative.

# Examples
# Example 1:
# Input: n=5
# Output: Positive

# Example2:
# Input: n=-6
# Output: Negative

def positive_negitive(n):
  if n > 0:
    print("Positive Number")
  else:
    print("Negitive Number")
n = int(input())
positive_negitive(n)