import matplotlib.pyplot as plt
import numpy as np

# Definindo a função f(n)
def funcao_f(n):
    return (n**3 / 1000) - 10 * n**2 - 100 * n + 3

# Gerando uma série de valores de n de 1 a 100
valores_de_n = np.arange(1, 101)

# Calculando f(n) para cada valor de n
resultados_f = [funcao_f(valor) for valor in valores_de_n]

# Criando um gráfico da função f(n)
plt.figure(figsize=(10, 6))
plt.plot(valores_de_n, resultados_f, label='f(n) = (n^3 / 1000) - 10n^2 - 100n + 3', color='red')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Comportamento de f(n) em relação a n')
plt.legend()
plt.grid(True)
plt.show()
