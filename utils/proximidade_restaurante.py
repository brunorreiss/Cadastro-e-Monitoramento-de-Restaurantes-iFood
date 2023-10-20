import math
from geopy import distance


#abordagem usando a geopy 
def proximidade_restaurante_geopy(coord_1: list, coord_2: list) -> float:    
    return round(distance.distance(coord_1, coord_2).km, 2)


#implementando o cálculo da distância utilizando a formula de Haversine
def proximidade_restaurante(coord_1: list, coord_2: list) -> float:
    # considerando que estamos no plano vamos utilizar a distância euclidiana
    # para realizar o cálculo da distância.
    raio_terra = 6371.0 # raio da terra em km

    # Converter graus para radianos
    lat1 = math.radians(coord_1[0])
    lat2 = math.radians(coord_2[0])

    lon1 = math.radians(coord_1[1])
    lon2 = math.radians(coord_2[1])

    # Fórmula de Haversine
    a = math.sin((lat2 - lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1)/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em quilômetros
    distance = round(raio_terra*c, 2)

    return distance

# Path: proximidade_restaurante.py


if __name__ == '__main__':
    print(f"A distância entre São Paulo e Rio de janeiro em Km é: {proximidade_restaurante_geopy((23.550278, -46.633889), (22.902778, -43.207778))}")
    print(f"A distância entre São Paulo e Rio de janeiro em Km é: {proximidade_restaurante((23.550278, -46.633889), (22.902778, -43.207778))}")
