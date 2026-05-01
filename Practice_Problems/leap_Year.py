# Check if given year is a leap year or not


# Problem Statement: Check if the given year is a leap year or not.

# Examples
# Example 1:
# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.

# Example 2:
# Input: 2000
# Output: Yes
# Explanation: Since 2000 is a leap year answer is “Yes”.
            
def leap_Year(n):
  if (n%4 == 0 or n%100 == 0 and n%400!=0):
    print("Leap Year")
  else:
    print("Not A Leap Year")
n = int(input())
(leap_Year(n))