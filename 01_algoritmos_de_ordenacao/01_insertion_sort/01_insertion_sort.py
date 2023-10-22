def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i] # Elemento atual a ser inserido na parte ordenada
    j = i - 1 # Comece a comparar com o elemento anterior

    # Mova os elementos maiores do que o elemento atual para a direita
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j-=1
    # Insira o elemento atual na posição correta
    arr[j+1] = key

lista = [12, 11, 13, 5, 6]
insertion_sort(lista)
print('Lista ordenada: ', lista)
