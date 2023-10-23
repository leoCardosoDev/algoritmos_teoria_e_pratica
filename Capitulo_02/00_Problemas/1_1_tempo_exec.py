import math

# Função para calcular o tempo em microssegundos para cada função f(n)
def calculate_time(func, n):
    return func(n)

# Funções para calcular o tempo de execução de cada função f(n)
def lg_n(n):
    return math.log2(n) * 1e6

def sqrt_n(n):
    return math.sqrt(n) * 1e6

def n(n):
    return n * 1e6

def n_lg_n(n):
    return n * math.log2(n) * 1e6

def n_squared(n):
    return n**2 * 1e6

def n_cubed(n):
    return n**3 * 1e6

def two_pow_n(n):
    return 2**n * 1e6

def n_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result * 1e6

# Defina o tempo disponível em microssegundos para cada intervalo de tempo
time_intervals = {
    "1 segundo": 1e6,
    "1 minuto": 60 * 1e6,
    "1 hora": 3600 * 1e6,
    "1 dia": 24 * 3600 * 1e6,
    "1 mês": 30 * 24 * 3600 * 1e6,
    "1 ano": 365 * 24 * 3600 * 1e6,
    "1 século": 100 * 365 * 24 * 3600 * 1e6
}

# Lista de funções e seus nomes
functions = [
    (lg_n, "lg n"),
    (sqrt_n, "√n"),
    (n, "n"),
    (n_lg_n, "n lg n"),
    (n_squared, "n²"),
    (n_cubed, "n³"),
    (two_pow_n, "2^n"),
    (n_factorial, "n!")
]

# Para cada função, calcule o maior tamanho n para cada intervalo de tempo
for func, func_name in functions:
    print(f"Tempo de execução para {func_name}:")
    for interval, t in time_intervals.items():
        n = None
        if func_name == "lg n":
            # Limite t para evitar estouro numérico
            t = min(t, 1e6 * 100)  # Limite para 100 segundos
            n = 2 ** (t / 1e6)
        elif func_name == "n!":
            # Evite a divisão por zero para n!
            n = 1
            while n_factorial(n) < t:
                n += 1
        else:
            n = t / func(1)
        print(f"{interval}: n <= {int(n)}")
    print()

