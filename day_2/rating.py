# 4. Product Rating Level
# Problem
# After buying a product, customers give ratings.
# Write a program that finds whether the product rating is excellent, average, or poor.
# Input
# rating
# Constraints
# ● 0 ≤ rating ≤ 5
# Example
# Input: 4.5 Output: Excellent Product
# Input: 3 Output: Average Product
# Input: 2 Output: Poor Product


def product(rating):
  if 0<= rating <=2:
    print("Poor")
  elif 2< rating <=3:
    print("Average")
  elif 3< rating <=5:
    print("Excellent")
rating = float(input())
product(rating)