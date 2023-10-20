import json
import math


class Restaurante:
    def __init__(self, nome, lat, lon, n_pedidos=0):
        self.nome = nome
        self.localidade = {'lat': lat, 'lon': lon}
        self.n_pedidos = n_pedidos
        self.cardapio = []
        self.historico_vendas = []


# Funções para manipulação de arquivos
def carregar_restaurantes():
    try:
        with open('restaurantes.json', 'r') as f:
            restaurantes = json.load(f)
            return [Restaurante(**restaurante) for restaurante in restaurantes]
    except FileNotFoundError:
        return []


def salvar_restaurantes(restaurantes):
    with open('restaurantes.json', 'w') as f:
        json.dump([restaurante.__dict__ for restaurante in restaurantes], f)

