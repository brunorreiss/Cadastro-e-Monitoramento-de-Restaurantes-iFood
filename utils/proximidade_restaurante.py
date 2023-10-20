# Import libs
import math


def verificar_proximidade(self, localidade):
    lat1, lon1 = localidade['lat'], localidade['lon']
    lat2, lon2 = self.localidade['lat'], self.localidade['lon']
    # Fórmula de Haversine para calcular a distância entre duas coordenadas
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c
    return distance
