# 6. Cart Item Limit
# Problem
# A shopping cart has a limit for the number of items.
# Write a program that checks whether a product can be added to the cart or not.
# Input
# cartItems
# Constraints
# ● 0 ≤ cartItems ≤ 20
# Example
# Input: 6 Output: Item Added to Cart
# Input: 12 Output: Cart Limit Reached


def cartLimit(item):
  if 0<= item <=11:
    print("Item added to cart")
  else:
    print("Cart Limit Reached")
item = int(input())
cartLimit(item)