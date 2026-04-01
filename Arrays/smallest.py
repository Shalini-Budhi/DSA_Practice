# // 1. Find the smallest element


def smallest_Elelment(arr):
  smallest = arr[0]
  for i in range(0, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
  return smallest

arr = list(map(int, input().split()))
print(smallest_Elelment(arr))