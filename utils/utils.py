import json
import uuid
import restaurante


def load_data(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(e)
    return data

def save_data(data: dict, file_path: str) -> None:
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    restaurantes = load_data("teste.json")
    id = str(uuid.uuid4())
    print(restaurantes)
    r1 = {
        "nome": "nome",
        "lat": 10,
        "lon": 20,
        "qtd_pedidos": 0,
        "cardapio": [
            {
                "nome_prouto": "nome_prouto",
                "categoria": "categoria",
                "alcoolico": "alcoolico",
                "valor": 10,
                "estoque": 20,
            }
        ],
    }

    r2 = restaurante.cadastrar_restaurante("Frutos do Mar e Cia", [10, 20])
    restaurantes[id] = r2
    save_data(restaurantes, "teste.json")
