# Problem
# 1.A shopping app wants to classify orders based on the order amount.
# Write a program that takes the order amount and finds whether the order is small, medium, or large.
# Input
# orderAmount
# Constraints
# ● 1 ≤ orderAmount ≤ 100000
# Example
# Input: 300 Output: Small Order
# Input: 1500 Output: Medium Order
# Input: 5000 Output: Large Order



def shopping(orderAmount):
  
  if orderAmount<1500:
    print("Small Order")
  elif orderAmount<5000:
    print("Medium Order")
  else:
    print("Large Order")
orderAmount = int(input())
shopping(orderAmount)