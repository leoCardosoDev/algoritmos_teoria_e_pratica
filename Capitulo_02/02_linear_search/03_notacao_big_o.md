## Ordenação por Seleção (Selection Sort)

A ordenação por seleção é um algoritmo simples de ordenação que classifica um array encontrando repetidamente o menor elemento restante e movendo-o para a posição correta no array. Abaixo está um código Python para a ordenação por seleção, juntamente com a explicação das características do algoritmo:

```python
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Encontra o índice do menor elemento restante no array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o menor elemento encontrado com a posição i
        arr[i], arr[min_index] = arr[min_index], arr[i]

**Invariante de Loop**: O invariante de loop deste algoritmo é que após cada iteração externa (ciclo principal), a parte inicial do array (à esquerda) estará ordenada. Em outras palavras, o menor elemento restante do array não classificado será movido para a posição correta no array classificado.

**Complexidade Temporal**:

- **Melhor Caso**: O melhor caso ocorre quando o array já está completamente ordenado, mas o algoritmo não tem conhecimento disso. Mesmo assim, ele verifica todos os elementos para garantir que o menor seja encontrado, o que resulta em \(O(n^2)\) operações de comparação.

- **Pior Caso**: O pior caso ocorre quando o array está em ordem reversa, forçando o algoritmo a fazer \(O(n^2)\) operações de comparação. Portanto, o pior caso também é \(O(n^2)\).

O motivo pelo qual o algoritmo só precisa ser executado para os primeiros \(n-1\) elementos é que, à medida que os primeiros \(n-1\) elementos são classificados, o último elemento é automaticamente colocado em sua posição correta. Portanto, não é necessário verificar e mover o último elemento.

A ordenação por seleção é um algoritmo de ordenação simples, mas não é eficiente para listas grandes, devido à sua complexidade \(O(n^2)\) no pior caso. Outros algoritmos de ordenação, como o Merge Sort e o Quick Sort, são mais eficientes em listas maiores.
