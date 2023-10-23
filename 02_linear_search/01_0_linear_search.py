def linear_search (arr, v):
  for i in range(len(arr)):
    if arr[i] == v:
      return i
  return 'NIL'

a = [10, 20, 30, 40, 50]
v = 30

# Invariante de Loop:
# A cada iteração, o algoritmo verifica se o elemento atual é igual a v. Se encontrar, retorna o índice i.

# Inicialização: Antes do loop, i = 0. O invariante de loop é satisfeito, pois o algoritmo verifica o primeiro elemento da sequência.

# Manutenção: Durante cada iteração, o algoritmo verifica se o elemento atual (arr[i]) é igual a v. Se for igual, retorna o índice i. Caso contrário, avança para o próximo elemento (i += 1) e continua a busca. O invariante de loop é mantido a cada iteração.

# Terminação: O loop termina quando i atinge o final da sequência. Nesse ponto, ou encontramos o valor v e retornamos o índice correto, ou não encontramos v e retornamos "NIL". O invariante de loop é satisfeito até o final.

# Executando a busca linear

result = linear_search(a,v)
if result != 'NIL':
  print(f'O valor {v} foi encontrado no indice {result}')
else:
  print(f'O valor {v} não foi encontrado na sequência')

v = 25
result = linear_search(a, v)
if result != 'NIL':
  print(f'O valor {v} foi encontrado no indice {result}')
else:
  print(f'O valor {v} não foi encontrado na sequência')
