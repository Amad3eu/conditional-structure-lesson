# Função para realizar a operação desejada
def calcular(valor1, valor2, operacao):
    if operacao == "+":
        return valor1 + valor2
    elif operacao == "-":
        return valor1 - valor2
    elif operacao == "*":
        return valor1 * valor2
    elif operacao == "/":
        if valor2 != 0:
            return valor1 / valor2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."


# Solicita os valores e a operação ao usuário
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza o cálculo e imprime o resultado
resultado = calcular(valor1, valor2, operacao)
print(f"O resultado da operação é: {resultado}")


