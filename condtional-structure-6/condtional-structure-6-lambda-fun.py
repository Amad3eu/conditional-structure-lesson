# Solicita o nome do corretor e o valor da venda
nome_corretor = input("Digite o nome do corretor: ")
valor_venda = float(input("Digite o valor da venda: "))

# Define uma função lambda para calcular a comissão
calcular_comissao = lambda valor: (
    valor * 0.095 if 30000 <= valor <= 50000 else valor * 0.07
)

# Calcula a comissão
comissao = calcular_comissao(valor_venda)

# Exibe o resultado
print(f"O corretor {nome_corretor} receberá uma comissão de R${comissao:.2f}.")
