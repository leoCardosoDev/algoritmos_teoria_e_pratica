def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return False

def find_sum_pair(arr, x):
  arr.sort() # Ordena o conjunto (melhor caso: Já ordenado)
  for i in range(len(arr)):
    diff = x - arr[i]
    if binary_search(arr, diff):
      return True
  return False

# Exemplo de melhor caso: par imediatamente encontrado
arr_best_case = [1, 2, 3, 4, 5]
x_best_case = 9
result_best_case = find_sum_pair(arr_best_case, x_best_case)
print(f'Melhor caso: Par encontrado? {result_best_case}')

# Exemplo de pior caso: nenhum par encontrado
arr_worst_case = [1, 2, 3, 4, 5]
x_worst_case = 10
result_worst_case = find_sum_pair(arr_worst_case, x_worst_case)
print(f'Pior caso: Par encontrado? {result_worst_case}')
