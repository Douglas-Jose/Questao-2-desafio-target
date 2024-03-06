def verifica_fibonacci(numero):
    if numero < 0:
        return f"{numero} não é um número válido para a sequência de Fibonacci."

    a, b = 0, 1

    # Caso especial para 0
    if numero == 0:
        return f"{numero} faz parte da sequência de Fibonacci."

    while b <= numero:
        if b == numero:
            return f"{numero} faz parte da sequência de Fibonacci."
        a, b = b, a + b

    return f"{numero} não faz parte da sequência de Fibonacci."


numero = int(input("Informe um número: "))
resultado = verifica_fibonacci(numero)
print(resultado)