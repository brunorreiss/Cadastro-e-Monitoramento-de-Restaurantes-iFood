def registrar_vendas(self, vendas=None):
    print("Digite a quantidade de vendas:")
    try:
        vendas = int(input())
        self.historico_vendas.append(vendas)
        self.n_pedidos += vendas
    except ValueError:
        print("Por favor, insira um número inteiro.")