import math
import utils
from geopy import distance


def cadastrar_restaurante(nome: str, coordenadas: list, n_pedidos=0) -> dict:
    cardapio = []
    cardapio = criar_cardapio(cardapio)
    restaurante = {
        "nome": nome,
        "lat": coordenadas[0],
        "lon": coordenadas[1],
        "qtd_pedidos": n_pedidos,
        "cardapio": cardapio,
    }
    return restaurante


def proximidade_restaurante(coord_1: list, coord_2: list) -> float:
    raio_terra = 6371.0  # raio da terra em km

    # Converter graus para radianos
    lat1 = math.radians(coord_1[0])
    lat2 = math.radians(coord_2[0])
    lon1 = math.radians(coord_1[1])
    lon2 = math.radians(coord_2[1])

    # Fórmula de Haversine
    a = (
        math.sin((lat2 - lat1) / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em quilômetros
    distance = round(raio_terra * c, 2)

    return distance


# abordagem usando a geopy
def proximidade_restaurante_geopy(coord_1: list, coord_2: list) -> float:
    return round(distance.distance(coord_1, coord_2).km, 2)


def criar_cardapio(items: list) -> list:
    print("Digite os itens do cardápio (digite 'sair' para terminar):")
    while True:
        """
        item_cardapio = {
            'nome_produto': str,
            'categoria': str,
            'alcoolico': str,
            'valor': float,
            'estoque': int,
        }
        """
        nome_produto = input("Nome do produto: ")
        if nome_produto.lower() == "sair":
            break
        categoria = input("Tipo do item (comida ou bebida): ").lower()
        alcoolico = bool(input("O item é alcoolico?: 1 - Sim, 0 - Não").lower())
        valor = float(input("Informe o valor do produto: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        items.append(
            {
                "nome_produto": nome_produto,
                "categoria": categoria,
                "alcoolico": alcoolico,
                "valor": valor,
                "estoque": estoque,
            }
        )
    return items


def fazer_pedido(cardapio, pedido) -> None:
    item = pedido
    if item in cardapio:
        print(f"Adicionando {item} ao seu pedido.")
        pedido.append(item)

def registrar_vendas(self, vendas=None) -> None:
    print("Digite a quantidade de vendas:")
    try:
        vendas = int(input())
        self.historico_vendas.append(vendas)
        self.n_pedidos += vendas
    except ValueError:
        print("Por favor, insira um número inteiro.")