import os
import platform
from src.restaurante import *
from src.json_manipulation import *

def clear() -> None:
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    while True:
        clear()
        print("Bem-vindo ao iFood!")
        print("O que você deseja fazer?")
        
        print("\n".join(
            [
                "1. Cadastrar novo restaurante",
                "2. Criar cardápio",
                "3. Registrar histórico de vendas",
                "4. Verificar restaurantes mais próximos",
                "5. Listar restaurantes",
                "6. Remover restaurante",
                "7. Atualizar número de pedidos",
                "8. Fazer pedido",
                "9. Sair"
            ]
        ))

        opcao = input("Escolha uma opção: ")

        restaurantes = load_data()

        if opcao == "1":
            nome = input("Nome do restaurante: ")
            lat = float(input("Latitude: "))
            lon = float(input("Longitude: "))
            restaurante = {
                'nome': nome,
                'coordenadas': [lat, lon],
                'pedidos': 0
            }
            salvar_restaurante(**restaurante)

        elif opcao == "2":
            nome = input("Nome do restaurante: ")
            
            id = None
            for chave in restaurantes:
                if restaurantes[chave].get('nome') == nome:
                    id = chave
                    break
            
            if id:
                restaurante = restaurantes[id]
                restaurante = criar_cardapio(restaurante)
                restaurante['id'] = id
                salvar_restaurante(**restaurante)
            else:
                print("Restaurante não encontrado.")

        # elif opcao == "3":
        #     pass

        elif opcao == "4":
            lat = float(input("Informe sua coordenada de latitude: "))
            lon = float(input("Informe sua coordenada de longitude: "))
            
            restaurantes_proximos = proximidade_restaurante(restaurantes, lat, lon)            
            restaurantes_proximos = sorted(restaurantes_proximos, key=lambda restaurante: restaurante['distancia'])
            
            for restaurante, distancia in restaurantes_proximos.items():
                print (f"Restaurante: {restaurante}, com a distância de {distancia} metros.")
            
            input('\nDigite qualquer tecla para continuar ...')

        elif opcao == "5":
            for id, restaurante in restaurantes.items():
                clear()
                for chave, valor in restaurante.items():
                    if chave == 'coordenadas':
                        print(f"{chave}: {valor[0]}, {valor[1]}")
                    elif chave == 'cardapio':
                        print(f"{chave}:")
                        for item in valor:
                            for nova_chave, novo_valor in item.items():
                                print(f"\t{nova_chave}: {novo_valor}")
                    elif chave == 'id':
                        continue
                    else:
                        print(f"{chave}: {valor}")
                input('\nDigite qualquer tecla para continuar ...')

        elif opcao == "6":
            print('Restaurantes cadastrados:')
            for _, restaurante in restaurantes.items():
                print(restaurante.get('nome'))
                
            nome = input("Nome do restaurante que deseja descadastrar: ")
            
            id = None
            for chave in restaurantes:
                if restaurantes[chave].get('nome') == nome:
                    id = chave
                    break
            
            if id:
                restaurantes.pop(id)
                save_data(restaurantes)
            else:
                print("Restaurante não encontrado.")

        elif opcao == "7":
            nome = input("Nome do restaurante: ")
            
            id = None
            for chave in restaurantes:
                if restaurantes[chave].get('nome') == nome:
                    id = chave
                    break
            
            if id:
                restaurante = restaurantes[id]
                restaurante = atualizar_pedidos()
                restaurante['id'] = id
                salvar_restaurante(**restaurante)
            else:
                print("Restaurante não encontrado.")
                
        # elif opcao == 8:
        #     pass

        elif opcao == "9":
            break

        else:
            print("Opção inválida!")