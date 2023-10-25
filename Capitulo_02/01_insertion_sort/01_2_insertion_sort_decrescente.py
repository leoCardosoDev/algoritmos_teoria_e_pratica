def insertion_sort_descending(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i -1
    while j >= 0 and key > arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

a = [31, 41, 59, 26, 41, 58]

insertion_sort_descending(a)
print('Array ordenado em ordem decrescente', a)
