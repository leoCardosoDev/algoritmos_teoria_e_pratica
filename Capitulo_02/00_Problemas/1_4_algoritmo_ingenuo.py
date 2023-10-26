def evaluate_polinomial_naive(coefficients, x):
  result = 0
  n = len(coefficients) - 1 # Grau do polinômio
  for i in range(n, -1, -1):
    result += coefficients[i] * (x ** 1)
  return result

# Exemplo de uso:
coefficients = [2, 3, 1] # Coeficientes do polinômio: 2x^2 + 3x + 1
x = 4
result = evaluate_polinomial_naive(coefficients, x)
print(f'Resultado = {result}')
