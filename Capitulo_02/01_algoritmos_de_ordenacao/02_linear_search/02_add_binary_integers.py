def add_binary_integers(a, b):
  n = len(a)
  carry = 0
  c = [0] * (n+1)
  for i in range(n -1, -1, -1):
    # Soma os digitos de a, b e carry
    total = a[i] + b[i] + carry
    # Atualiza o digito resultante em c
    c[i+1] = total % 2
    # Calcula o carry para a proxima interação
    carry = total // 2
  # O digito mais significativos (MSB) de c pode conter um carry
  c[0] = carry
  return c

# Exemplo de entrada
a = [1, 0, 1, 1] # Representa o número binário 1011
b = [1, 1, 0, 1] # Representa o número binário 1101

result = add_binary_integers(a, b)
print('O resultado da soma em binario é: ', result)
