import os
import json
from uuid import uuid4

DEFAULT_FILE_PATH = "./database/json_db.json"

def load_data(file_path: str = DEFAULT_FILE_PATH) -> dict:
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def save_data(data: dict, file_path: str = DEFAULT_FILE_PATH) -> None:
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
def salvar_restaurante(**restaurante: dict) -> None:
    restaurantes = load_data()
    
    if restaurante.get('id'):
        id = restaurante.get('id')
    else:
        id = str(uuid4())
    restaurantes[id] = restaurante
    save_data(restaurantes)