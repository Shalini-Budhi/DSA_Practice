# 5. Return Policy Check
# Problem
# Products can be returned only within a certain number of days.
# Write a program that checks whether the product can be returned or not.
# Input
# daysAfterDelivery
# Constraints
# ● 0 ≤ days ≤ 30
# Example
# Input: 5 Output: Return Allowed
# Input: 12 Output: Return Not Allowed

# def returnPolicy(days):
#   if days <= 5:
#     print("Return Allowed")
#   else:
#     print("Return Not Allowed")
# days = int(input())
# returnPolicy(days) 


def returnPolicy(days):
  limit = 5
  if days <= limit:
    print("return Allowed")
  else:
    print("Return Not Allowed")
days = int(input())
returnPolicy(days)