def merge(arr, left_start, middle, right_end):
    n1 = middle - left_start + 1
    n2 = right_end - middle

    # Crie arranjos temporários para a esquerda (left) e direita (right)
    left = [0] * n1
    right = [0] * n2

    # Copie os elementos do arranjo original para os arranjos temporários left e right
    for i in range(n1):
        left[i] = arr[left_start + i]
    for j in range(n2):
        right[j] = arr[middle + 1 + j]

    i, j, k = 0, 0, left_start

    # Combine os arranjos left e right de volta no arranjo original
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copie os elementos restantes de left (se houver)
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copie os elementos restantes de right (se houver)
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

# Exemplo de uso
arr = [3, 41, 52, 26, 38, 57, 9, 49]
merge(arr, 0, 3, 7)

print("Array após a mesclagem:", arr)
