def binary_search(arr, target):
  left, right = 0, len(arr) -1
  while left <= right:
    mid = left + (right - left) // 2 # Evita o estouro em arrays muito grandes
    if arr[mid] == target:
      return mid # Elemento encontrado, retorna o indice
    elif arr[mid] < target:
      left = mid + 1 # Reduz a busca para a metade direita
    else:
      right = mid - 1
  return -1 # Elemento não encontrado

# Exemplo de uso 
arr = [3, 9, 26, 38, 41, 49, 52, 57]
target = 38
result = binary_search(arr, target)

if result != -1:
  print(f'O valor {target} foi encontrado no indice {result}')
else:
  print(f'O valor {target} não foi encontrado na sequência.')
