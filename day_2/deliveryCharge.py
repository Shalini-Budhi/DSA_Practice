# 3. Free Delivery Check
# Problem
# The shopping app gives free delivery for high-value orders.
# Write a program to check whether the order is eligible for free delivery.
# Input
# orderAmount
# Constraints
# ● 1 ≤ orderAmount ≤ 100000
# Example
# Input: 900 Output: Free Delivery
# Input: 400 Output: Delivery Charges Apply


def deliveryCharge(amount):
  if amount>=900:
    print("Free Delivery")
  else:
    print("Delivery Charges Apply")
amount = int(input())
deliveryCharge(amount)