def soma_binarios_inteiros(binario_a, binario_b):
    tamanho = len(binario_a)
    carry = 0
    resultado = [0] * (tamanho + 1)
    
    for i in range(tamanho - 1, -1, -1):
        # Soma os dígitos de binario_a, binario_b e carry
        total = binario_a[i] + binario_b[i] + carry
        # Atualiza o dígito resultante em resultado
        resultado[i + 1] = total % 2
        # Calcula o carry para a próxima iteração
        carry = total // 2
    
    # O dígito mais significativo (MSB) de resultado pode conter um carry
    resultado[0] = carry
    
    return resultado

# Exemplo de entrada
binario_a = [1, 0, 1, 1]  # Representa o número binário 1011
binario_b = [1, 1, 0, 1]  # Representa o número binário 1101

resultado_soma = soma_binarios_inteiros(binario_a, binario_b)
print('O resultado da soma em binário é:', resultado_soma)
