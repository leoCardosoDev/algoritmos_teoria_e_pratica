def merge(arr, inicio, meio, fim):
    tamanho_subarray1 = meio - inicio + 1  # Comprimento do primeiro subarray
    tamanho_subarray2 = fim - meio       # Comprimento do segundo subarray

    # Crie arrays temporários para os subarrays
    subarray_esquerda = [0] * (tamanho_subarray1 + 1)
    subarray_direita = [0] * (tamanho_subarray2 + 1)

    # Copie os elementos dos subarrays originais para os temporários
    for i in range(tamanho_subarray1):
        subarray_esquerda[i] = arr[inicio + i]
    for j in range(tamanho_subarray2):
        subarray_direita[j] = arr[meio + 1 + j]

    # Defina sentinelas no final dos subarrays temporários
    subarray_esquerda[tamanho_subarray1] = float('inf')  # Sentinela para subarray esquerda
    subarray_direita[tamanho_subarray2] = float('inf')  # Sentinela para subarray direita

    # Combine os subarrays ordenados de volta no array principal
    i = j = 0
    for k in range(inicio, fim + 1):
        if subarray_esquerda[i] <= subarray_direita[j]:
            arr[k] = subarray_esquerda[i]
            i += 1
        else:
            arr[k] = subarray_direita[j]
            j += 1

# Exemplo de uso
array_original = [3, 6, 8, 10, 2, 1, 4, 7]
merge(array_original, 0, 3, 7)
print(array_original)  # Saída: [1, 2, 3, 4, 6, 7, 8, 10]
