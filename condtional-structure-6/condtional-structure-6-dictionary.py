# Solicita o nome do corretor e o valor da venda
nome_corretor = input("Digite o nome do corretor: ")
valor_venda = float(input("Digite o valor da venda: "))

# Define as taxas de comissão em um dicionário
faixas_comissao = {
    'normal': 0.07,
    'especial': 0.095
}

# Verifica a faixa de comissão
faixa = 'especial' if 30000 <= valor_venda <= 50000 else 'normal'

# Calcula a comissão
comissao = valor_venda * faixas_comissao[faixa]

# Exibe o resultado
print(f"O corretor {nome_corretor} receberá uma comissão de R${comissao:.2f}.")
