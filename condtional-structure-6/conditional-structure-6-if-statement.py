# Solicita o nome do corretor e o valor da venda
nome_corretor = input("Digite o nome do corretor: ")
valor_venda = float(input("Digite o valor da venda: "))

# Calcula a comissão com base no valor da venda
if 30000 <= valor_venda <= 50000:
    comissao = valor_venda * 0.095
else:
    comissao = valor_venda * 0.07

# Exibe o resultado
print(f"O corretor {nome_corretor} receberá uma comissão de R${comissao:.2f}.")
