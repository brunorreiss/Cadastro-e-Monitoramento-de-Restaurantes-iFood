import math
from uuid import uuid4

def cadastrar_restaurante(**kwargs) -> dict:
    restaurante = {
        "nome": kwargs.get('nome'),
        "coordenadas": kwargs.get('coordenadas'),
        "historico_vendas": kwargs.get('historico_vendas'),
        "pedidos": kwargs.get('pedidos'),
        "cardapio": kwargs.get('cardapio'),
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
            if alcoolico == '1':
                alcoolico = True
            else:
                alcoolico = False
                
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

def atualizar_estoque(restaurante: dict, idx: int, qtd: int) -> dict:
    restaurante['cardapio'][idx]['estoque'] = qtd
    return restaurante

def proximidade_restaurante(restaurantes: dict, lat_user: float, lon_user: float) -> list:
    raio_terra = 6371.0  # raio da terra em km
    restaurantes_proximo = []
    for restaurante in restaurantes.values():
        # Converter graus para radianos
        lat1 = math.radians(restaurante.get("coordenadas")[0])
        lat2 = math.radians(lat_user)
        lon1 = math.radians(restaurante.get("coordenadas")[1])
        lon2 = math.radians(lon_user)
    
        # Fórmula de Haversine
        a = (
            math.sin((lat2 - lat1) / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distância em quilômetros
        distance = round(raio_terra * c, 2)                                   
        restaurantes_proximo.append({ 
            'nome': restaurante['nome'], 
            'distancia': distance
        } )
    return restaurantes_proximo

    
def realizar_pedido(restaurante: dict, **kwargs) -> None:
    """
    'id_pedido': str,
    'user_name': str,
    'user_phone': str,
    'user_coordenadas': [lat, lon],
    'qtd': int,
    'total_pedido': float
    """
    id_pedido = str(uuid4())
    user_name = kwargs.get('user_name')
    user_phone = kwargs.get('user_phone')
    user_coordenadas = kwargs.get('user_coordenadas')
    nome_produto = kwargs.get('nome_produto')
    qtd = kwargs.get('qtd')
    total_pedido = round(restaurante.get('cardapio')[kwargs.get('indice')].get('valor')*qtd, 2)
    restaurante.get('cardapio')[kwargs.get('indice')]['estoque'] -= qtd
    restaurante['pedidos'] += 1 
    dict_pedido = {
        'id_pedido': id_pedido,
        'user_name': user_name,
        'user_phone': user_phone,
        'user_coordenadas': user_coordenadas,
        'nome_produto': nome_produto,
        'qtd': qtd,
        'total_pedido': total_pedido
    }
    restaurante['historico_vendas'].append(dict_pedido)
    return restaurante
