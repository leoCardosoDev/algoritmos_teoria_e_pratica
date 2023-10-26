def insertion_sort(sublist):
  for i in range(1, len(sublist)):
    current_element = sublist[i]
    j = i -1
    while j >= 0 and current_element < sublist[j]:
      sublist[j + 1] = sublist[j]
      j -= 1
    sublist[j + 1] = current_element


def merge(arr, left, right):
  i = j = k = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1
  
  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1
  
  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1


def modified_merge_sort(arr, insertion_threshold):
  if len(arr) <= insertion_threshold:
    insertion_sort(arr)
  else:
    middle = len(arr) // 2
    left_sublist = arr[:middle]
    right_sublist = arr[middle:]

    modified_merge_sort(left_sublist, insertion_threshold)
    modified_merge_sort(right_sublist, insertion_threshold)

    merge(arr, left_sublist, right_sublist)

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
insertion_threshold = 5

modified_merge_sort(arr, insertion_threshold)
print('Array ordenado:', arr)
