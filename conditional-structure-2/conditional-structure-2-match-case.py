def calcular(valor1, valor2, operacao):
    match operacao:
        case "+":
            return valor1 + valor2
        case "-":
            return valor1 - valor2
        case "*":
            return valor1 * valor2
        case "/":
            return (
                valor1 / valor2
                if valor2 != 0
                else "Erro: Divisão por zero não é permitida."
            )
        case _:
            return "Erro: Operação inválida."


# Solicita os valores e a operação ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza o cálculo e imprime o resultado
resultado = calcular(valor1, valor2, operacao)
print(f"O resultado da operação é: {resultado}")
