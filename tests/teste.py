import sys
sys.path.insert(1, '../')

from src.restaurante import restaurante as rt
from src.menu import menu

print(f"A distância entre São Paulo e Rio de janeiro em Km é: {rt.proximidade_restaurante_geopy((23.550278, -46.633889), (22.902778, -43.207778))}")
print(f"A distância entre São Paulo e Rio de janeiro em Km é: {rt.proximidade_restaurante((23.550278, -46.633889), (22.902778, -43.207778))}")
