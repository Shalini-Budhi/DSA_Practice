# arr = [2,0,2,1,1,0]

def minNumber(arr):
  for i in range(len(arr)):
    min_element = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min_element]:
        min_element = j
    arr[i],arr[min_element] = arr[min_element],arr[i]
  return arr

arr = [2,0,2,1,1,0]
print(minNumber(arr))