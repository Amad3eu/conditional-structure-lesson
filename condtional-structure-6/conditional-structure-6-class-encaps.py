class Corretor:
    def __init__(self, nome, valor_venda):
        self.nome = nome
        self.valor_venda = valor_venda

    def calcular_comissao(self):
        return (
            self.valor_venda * 0.095
            if 30000 <= self.valor_venda <= 50000
            else self.valor_venda * 0.07
        )


# Solicita o nome do corretor e o valor da venda
nome_corretor = input("Digite o nome do corretor: ")
valor_venda = float(input("Digite o valor da venda: "))

# Cria uma instância da classe Corretor
corretor = Corretor(nome_corretor, valor_venda)

# Calcula a comissão
comissao = corretor.calcular_comissao()

# Exibe o resultado
print(f"O corretor {corretor.nome} receberá uma comissão de R${comissao:.2f}.")
