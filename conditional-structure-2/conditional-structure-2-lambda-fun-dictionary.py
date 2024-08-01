def calcular(valor1, valor2, operacao):
    # Define as operações em um dicionário
    operacoes = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: (
            x / y if y != 0 else "Erro: Divisão por zero não é permitida."
        ),
    }

    # Executa a operação desejada se for válida, caso contrário, retorna um erro
    return operacoes.get(operacao, lambda x, y: "Erro: Operação inválida.")(
        valor1, valor2
    )


# Solicita os valores e a operação ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza o cálculo e imprime o resultado
resultado = calcular(valor1, valor2, operacao)
print(f"O resultado da operação é: {resultado}")
