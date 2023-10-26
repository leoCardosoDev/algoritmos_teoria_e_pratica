def evaluate_polynominal(coefficients, x):
  result = coefficients[-1] # Inicializa o acumulador com o coeficiente de maior grau
  for coef in reversed(coefficients[:-1]):  # Percorre os coeficientes em ordem reversa, excluindo o coeficiente de maior grau
    result = result * x + coef # Aplica a regra de Horner
  return result

coefficients = [3, -1, 2, 0, 5 ] # Coeficientes do polinômio: 3x^4 - x^3 + 2x^2 + 5
x_value = 2.5 # Ponto em que desejamos avaliar o polinômio
result = evaluate_polynominal(coefficients, x_value)
print(f'O valor do polinômio em x = {x_value} é {result}')
