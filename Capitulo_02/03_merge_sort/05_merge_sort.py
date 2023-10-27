def count_inversions(arr):
  if len(arr) <= 1:
    return arr, 0
  
  mid = len(arr) // 2
  left, inversions_left = count_inversions(arr[:mid])
  right, inversions_right = count_inversions(arr[mid:])
  merged, split_inversions = merge_and_count(left, right)
  total_inversions = inversions_left + inversions_right + split_inversions

  return merged, total_inversions


def merge_and_count(left, right):
  merged = []
  i = j = split_inversions = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
      split_inversions += len(left) - i
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged, split_inversions

# Exemplos de uso
arr = [2, 3, 8, 6, 1]
arr2 = [2, 3, 8, 6, 1]
sorted_arr, inversions = count_inversions(arr2)
print('Numeros de inversões', inversions)
