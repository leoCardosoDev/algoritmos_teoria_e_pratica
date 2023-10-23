import matplotlib.pyplot as plt
import numpy as np

# Função f(n)
def f(n):
    return (n**3 / 1000) - 10 * n**2 - 100 * n + 3

# Valores de n
n = np.arange(1, 101)  # Vamos considerar n de 1 a 100

# Calcula f(n) para cada valor de n
result = [f(i) for i in n]

# Plot da função f(n)
plt.figure(figsize=(10, 6))
plt.plot(n, result, label='f(n) = (n^3 / 1000) - 10n^2 - 100n + 3', color='red')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Comportamento de f(n) em relação a n')
plt.legend()
plt.grid(True)
plt.show()
