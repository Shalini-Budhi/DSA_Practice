# 7. Temperature Category
# Problem
# Write a program that determines the temperature category based on the given temperature value.

# Input
# temperature
# Constraints
# - -10 ≤ temperature ≤ 50
# Example
# Input: 15
# Output: Cold
# Input: 22
# Output: Warm
# Input: 30
# Output: Hot

def temperature_category(temp):
  
  if temp <= 15:
    print("Cold")
  elif temp <= 22:
    print("Warm")
  elif temp <= 25:
    print("Hot")
temp = int(input())
temperature_category(temp)


# def temperature_category(temp):
  
#   if temp == 15:
#     print("Cold")
#   elif temp == 22:
#     print("Warm")
#   elif temp == 25:
#     print("Hot")
# temp = int(input())
# temperature_category(temp)
 