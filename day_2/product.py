# 2. Product Stock Check
# Problem
# When a user opens a product page, the app should check if the product is available.
# Write a program that takes stock quantity and finds whether the product is available or out of stock.
# Input
# stock
# Constraints
# ● 0 ≤ stock ≤ 1000
# Example
# Input: 10 Output: Product Available
# Input: 0 Output: Out of Stock


# def products(stock):
#   if stock >0:
#     print("Product Available")
#   else:
#     print("Out of stock")
# stock = int(input())
# products(stock)


def product(stock):
  return "product Available" if stock > 0  else "Out of Stock"
stock = int(input())
print(product(stock))

