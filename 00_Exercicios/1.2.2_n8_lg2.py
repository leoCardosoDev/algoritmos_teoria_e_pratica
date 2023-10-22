import math
from scipy.optimize import fsolve

# Defina a função que represente a desigualdade:
def equation(n):
  return n - 8 * math.log2(n)

# Use o fsolve do SciPy para encontrar uma solução aproximada
approximate_solution = fsolve(equation, 1)

print(f'Aproximação da solução: n = {approximate_solution[0]}')
