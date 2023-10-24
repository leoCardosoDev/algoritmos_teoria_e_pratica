import math
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o tempo em microssegundos para cada função f(n)
def calcular_tempo(func, n):
    return func(n)

# Funções para calcular o tempo de execução de cada função f(n)
def tempo_logaritmico(n):
    return math.log2(n) * 1e6

def tempo_raiz_quadrada(n):
    return math.sqrt(n) * 1e6

def tempo_linear(n):
    return n * 1e6

def tempo_n_log_n(n):
    return n * math.log2(n) * 1e6

def tempo_quadrado(n):
    return n**2 * 1e6

def tempo_cúbico(n):
    return n**3 * 1e6

def tempo_exponencial(n):
    return 2**n * 1e6

def tempo_fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado * 1e6

# Defina o tempo disponível em microssegundos para cada intervalo de tempo
intervalos_de_tempo = {
    "1 segundo": 1e6,
    "1 minuto": 60 * 1e6,
    "1 hora": 3600 * 1e6,
    "1 dia": 24 * 3600 * 1e6,
    "1 mês": 30 * 24 * 3600 * 1e6,
    "1 ano": 365 * 24 * 3600 * 1e6,
    "1 século": 100 * 365 * 24 * 3600 * 1e6
}

# Lista de funções e seus nomes
funcoes = [
    (tempo_logaritmico, "lg n"),
    (tempo_raiz_quadrada, "√n"),
    (tempo_linear, "n"),
    (tempo_n_log_n, "n lg n"),
    (tempo_quadrado, "n²"),
    (tempo_cúbico, "n³"),
    (tempo_exponencial, "2^n"),
    (tempo_fatorial, "n!")
]

# Para cada função, calcule o maior tamanho n para cada intervalo de tempo
resultados = []
for func, nome_func in funcoes:
    tempos = []
    for intervalo, t in intervalos_de_tempo.items():
        n = None
        if nome_func == "lg n":
            # Limite t para evitar estouro numérico
            t = min(t, 1e6 * 100)  # Limite para 100 segundos
            n = 2 ** (t / 1e6) if t > 0 else 0
        elif nome_func == "n!":
            # Evite a divisão por zero para n!
            n = 1
            while tempo_fatorial(n) < t:
                n += 1
        else:
            n = t / func(1) if func(1) > 0 else 0
        tempos.append(int(n))
    resultados.append((nome_func, tempos))

# Gere um gráfico para cada função
plt.figure(figsize=(12, 8))
for nome_func, tempos in resultados:
    plt.plot(list(intervalos_de_tempo.keys()), tempos, marker='o', label=nome_func)

plt.xlabel('Intervalo de Tempo')
plt.ylabel('Tamanho de n')
plt.title('Estimativa de Tamanho de n para Diferentes Funções')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
