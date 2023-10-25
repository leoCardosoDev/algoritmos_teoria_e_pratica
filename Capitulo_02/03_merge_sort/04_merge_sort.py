import math

def solve_recurrence(n):
  if n == 2:
    return 2 # Caso base
  # Aplicando a recorrencia T(n) = 2T(n/2) + n
  return 2 * solve_recurrence(n // 2) + n

# Função para calcular o logaritmo na base 2
def log2(n):
  return math.log(n,2)

# Verificando para várias potencias de 2
for n in [2, 4, 8, 16, 32, 64]:
  result = solve_recurrence(n)
  expected = n * log2(n)
  print(f'Para n = {n}, T(n) = {result}, esperado: {expected}')
