def cyclicSort(arr):

  i = 0
  while i < len(arr):
    current_index = arr[i] - 1
    if arr[i] != arr[current_index]:
      arr[i],arr[current_index] = arr[current_index],arr[i]
    else:
      i += 1
  return arr
arr = [3,2,5,1,4]
print(cyclicSort(arr))

# Cyclic Sort is mainly used to sort numbers in an array.
# In Cyclic Sort, each number has a correct index position.
# The correct index of a number is calculated as number - 1.
# If the number is not at its correct index, we swap it with the number at the correct index.
# After the swap, we check the same index again until the number is in its correct position.
# Once the number is in the correct position, we move to the next index.