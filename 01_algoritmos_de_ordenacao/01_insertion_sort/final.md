# Insertion Sort em Python
Este é um exemplo de implementação do algoritmo de ordenação Insertion Sort em Python.

## Código Python

```python
def insertion_short(names):
    for i in range(1, len(names)):
        name = names[i]
        j = i - 1
        while j >= 0 and name < names[j]:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = name

nomes = ['João', 'José', 'Maria', 'Augusto', 'Robson', 'Wesley', 'Leo']
insertion_short(nomes)
print('Nomes ordenados:', nomes)

## Explicação do Código

- `insertion_short(names)`: Esta função implementa o algoritmo de ordenação Insertion Sort para ordenar uma lista de nomes em ordem alfabética crescente.

- O loop `for` itera sobre os índices da lista `names`, começando em 1, porque o primeiro elemento (índice 0) é considerado a parte ordenada inicialmente.

- A variável `name` armazena o elemento atual a ser inserido na parte ordenada da lista.

- A variável `j` é usada para comparar o elemento `name` com os elementos à esquerda na parte ordenada da lista.

- O loop `while` executa enquanto `j` for maior ou igual a zero e enquanto o elemento `name` for menor do que o elemento na posição `j` da lista `names`.

- O elemento na posição `j` é movido uma posição à direita na lista `names`, criando espaço para inserir o elemento `name` na posição correta.

- Após o loop `while`, o elemento `name` é inserido na posição `j + 1` na lista `names`, que é a posição correta na parte ordenada.

- A lista `nomes` é definida com nomes desordenados.

- A função `insertion_short` é chamada para ordenar a lista.

- A lista `nomes` agora ordenada é impressa na tela, mostrando os nomes em ordem alfabética crescente.

Este é um exemplo simples de como usar o Insertion Sort para ordenar uma lista de nomes em Python. O algoritmo é especialmente útil para listas pequenas ou quando a maioria dos elementos já está parcialmente ordenada.

