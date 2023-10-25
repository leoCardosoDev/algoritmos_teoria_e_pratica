def merge_sort(arr):
  if len(arr) <=1:
    return arr
  
  # Divide o array ao meio
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursivamente ordena as metades
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  # Inicializa indices para pecorrer as duas metades e o indice para o novo array
  left_index, right_index, result_index = 0, 0, 0

  # Mescla as metades ordenadas em um único array
  while left_index < len(left_half) and right_index < len(right_half):
    if left_half[left_index] < right_half[right_index]:
      arr[result_index] = left_half[left_index]
      left_index += 1
    else:
      arr[result_index] = right_half[right_index]
      right_index += 1
    result_index += 1

  # Copia quaisquer elementos restantes das metades (caso tenha sobrado)
  while left_index < len(left_half):
    arr[result_index] = left_half[left_index]
    left_index += 1
    result_index += 1
  
  while right_index < len(right_half):
    arr[result_index] = right_half[right_index]
    right_index += 1
    result_index += 1
  
  return arr


# Array de entrada
a = [3, 41, 52, 26, 38, 57, 9, 49]

# Ordena o array usando o merge_sort(a)
sorted_array = merge_sort(a)
print('Array original: ', a)
print('Array ordenado com merge sort: ', sorted_array)
