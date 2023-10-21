import math
from uuid import uuid4
from geopy import distance

def cadastrar_restaurante(**dict) -> dict:
    restaurante = {
        "nome": dict.get('nome'),
        "lat": dict.get('coordenadas')[0],
        "lon": dict.get('coordenadas')[0],
        "pedidos": dict.get('pedidos'),
        "cardapio": dict.get('cardapio'),
    }
    return restaurante

def criar_cardapio(restaurante: dict) -> dict:
    items = restaurante.get('cardapio')
    if not items:
        items = []
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
        if categoria == 'sair':
            break
        alcoolico = input("O item é alcoolico?\n1 - Sim, 0 - Não\n").lower()
        if alcoolico == 'sair':
            break
        else:
            alcoolico = bool(alcoolico)
        valor = input("Informe o valor do produto: ")
        if valor == 'sair':
            break
        else:
            valor = float(valor)
        estoque = input("Informe a quantidade em estoque: ")
        if estoque == 'sair':
            break
        else:
            estoque = int(estoque)
        items.append(
            {
                "nome_produto": nome_produto,
                "categoria": categoria,
                "alcoolico": alcoolico,
                "valor": valor,
                "estoque": estoque,
            }
        )
        
    restaurante['cardapio'] = items
    return restaurante

def atualizar_pedidos(restaurante: dict) -> dict:
    pedidos = restaurante.get('pedidos')
    
    print("Digite a quantidade de pedidos:")
    try:
        novos_pedidos = int(input())
    except ValueError:
        print("Por favor, insira um número inteiro.")
        
    pedidos += novos_pedidos
    restaurante['pedidos'] = pedidos
    return restaurante

# ------------------------------------------

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

def fazer_pedido(cardapio, pedido) -> None:
    item = pedido
    if item in cardapio:
        print(f"Adicionando {item} ao seu pedido.")
        pedido.append(item)
