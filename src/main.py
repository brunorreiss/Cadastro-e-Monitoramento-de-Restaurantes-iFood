import os
import platform
from src.restaurante import *
from src.json_manipulation import *

def clear() -> None:
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu_principal():
    while True:
        print("\n".join(
                [
                    "1. Acessar como parceiro;",
                    "2. Acessar como usuário;",
                    "3. Sair! "
                ]
            ))
        menu_switch = input('Escolha uma opção: ')

        if menu_switch == '1':
            menu_parceiro()
        elif menu_switch == '2':
            menu_user()
        elif menu_switch == '3':
            break


def menu_parceiro():
    while True:
        clear()
        print("Bem-vindo ao iFood!")
        print("O que você deseja fazer?")
        
        print("\n".join(
            [
                "1. Cadastrar novo restaurante",
                "2. Criar cardápio",
                "3. Ver histórico de vendas",
                "4. Listar restaurantes",
                "5. Remover restaurante",
                "6. Atualizar estoque",
                "7. Sair"
            ]
        ))

        opcao = input("Escolha uma opção: ")

        restaurantes = load_data()

        if opcao == "1":
            nome = input("Nome do restaurante: ")
            lat = float(input("Latitude: "))
            lon = float(input("Longitude: "))
            restaurante = cadastrar_restaurante(**{
                'nome': nome,
                'coordenadas': [lat, lon],
                'pedidos': 0,
                'cardapio': [],
                'historico_vendas': []
            })
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

        elif opcao == "3":
            for id, restaurante in restaurantes.items():
                clear()
                for chave, valor in restaurante.items():
                    if chave == 'historico_vendas':
                        if valor :
                            for item in valor:
                                for nova_chave, novo_valor in item.items():
                                    if nova_chave in ['user_name', 'nome_produto', 'qtd', 'total_pedido']:
                                        print(f'{nova_chave}: {novo_valor}')
                                print()
                        else:
                            print('Não há histórico de compras para o restaurante!')           
                    else:
                        continue
                input('\nDigite qualquer tecla para continuar ...')

        elif opcao == "4":
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
                    elif chave in ['id', 'pedidos', 'historico_vendas' ]:
                        continue
                    else:
                        print(f"{chave}: {valor}")
                input('\nDigite qualquer tecla para continuar ...')

        elif opcao == "5":
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

        elif opcao == "6":
            print('Restaurantes:')
            for _, restaurante in restaurantes.items():
                print(restaurante.get('nome'))
                
            nome = input("\nNome do restaurante que deseja selecionar: ")
            
            id = None
            for chave in restaurantes:
                if restaurantes[chave].get('nome') == nome:
                    id = chave
                    break
            
            if id:
                restaurante_selecionado = restaurantes.get(id)
                for item in restaurante_selecionado['cardapio']:
                  for key, value in item.items():
                        print(f"{key}: {value}")
                nome_produto = input('Qual o nome do produto que deseja comprar: ')
                qtd = int(input(f'Qual nova quantidade do produto {nome_produto} deseja adicionar: '))
                for idx, item in enumerate(restaurante_selecionado['cardapio']):
                    if item.get('nome_produto') == nome_produto:
                        restaurante_atualizado = atualizar_estoque(restaurante_selecionado, idx, qtd)
                        restaurante_atualizado['id'] = id                        
                        salvar_restaurante(**restaurante_atualizado)
                        break

                else:
                    print('Produto não existe no cardapio!') 
                
            else:
                print("Restaurante não encontrado.")

        elif opcao == "7":
            break

        else:
            print("Opção inválida!")


def menu_user():
    clear()
    user_name = input('Insira seu nome: ')
    user_telefone = input('Insira seu numero telefonico: ')
    user_latitude, user_longitude = float(input('Insira sua latitude: ')), float(input('Insira sua longitude: '))

    restaurantes = load_data()
    while True:
        print("\n".join(
                    [
                        "1. Encontrar restaurantes proximos;",
                        "2. Realizar pedido;",
                        "3. Sair! "
                    ]
                ))
        user_option = input('Escolha uma opção: ')

        
        if user_option == '3':
            print('Obrigado pelo seu acesso!')
            break

        
        elif user_option == '1':  
            restaurantes_proximos = proximidade_restaurante(restaurantes, user_latitude, user_longitude)            
            restaurantes_proximos = sorted(restaurantes_proximos, key=lambda restaurante: restaurante['distancia'])          
            count = 0
            for restaurante in restaurantes_proximos:
                if count == 5:
                    break
                print (f"Restaurante: {restaurante['nome']}, com a distância de {restaurante['distancia']} metros.")
                count += 1
            input('\nDigite qualquer tecla para continuar ...')

        elif user_option == '2':
            print('Restaurantes:')
            for _, restaurante in restaurantes.items():
                print(restaurante.get('nome'))
                
            nome = input("\nNome do restaurante realizar um pedido: ")
            
            id = None
            for chave in restaurantes:
                if restaurantes[chave].get('nome') == nome:
                    id = chave
                    break
            
            if id:
                restaurante_selecionado = restaurantes.get(id)
                for item in restaurante_selecionado['cardapio']:
                  for key, value in item.items():
                        print(f"{key}: {value}")
                nome_produto = input('Qual o nome do produto que deseja comprar: ')
                qtd = int(input('Qual a quantidade que deseja comprar: '))
                status = False
                idx = None
                for i, item in enumerate(restaurante_selecionado['cardapio']):
                    if item.get('nome_produto') == nome_produto:
                      if item.get('estoque') >= qtd:
                          status = True
                          idx = i
                          break
                      else:
                          print('Quantidade não disponível em estoque!')
                
                if status:
                    dicionario = {
                        'indice': idx,                        
                        'user_name': user_name,
                        'user_phone': user_telefone,
                        'user_coordenadas': [user_latitude, user_longitude],
                        'nome_produto': nome_produto,
                        'qtd': qtd,
                    }
                    restaurante_selecionado = realizar_pedido(restaurante_selecionado, **dicionario)
                    restaurante_selecionado['id'] = id
                    salvar_restaurante(**restaurante_selecionado)

                else:
                    print('Produto não existe no cardapio!') 
                
            else:
                print("Restaurante não encontrado.")            



if __name__ == "__main__":
    menu_principal()           