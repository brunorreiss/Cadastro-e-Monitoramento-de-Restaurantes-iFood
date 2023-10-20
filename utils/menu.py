def menu(restaurante, cardapio, historico_vendas, localidade, n_pedidos, carregar_restaurantes, salvar_restaurantes):
    restaurantes = carregar_restaurantes()

    while True:
        print("1. Cadastrar novo restaurante")
        print("2. Criar cardápio")
        print("3. Registrar histórico de vendas")
        print("4. Verificar restaurantes mais próximos")
        print("5. Listar restaurantes")
        print("6. Remover restaurante")
        print("7. Atualizar número de pedidos")
        print("8. Fazer pedido")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do restaurante: ")
            lat = float(input("Latitude: "))
            lon = float(input("Longitude: "))
            restaurante = Restaurante(nome, lat, lon)
            restaurantes.append(restaurante)
            salvar_restaurantes(restaurantes)

        elif opcao == "2":
            nome = input("Nome do restaurante: ")
            restaurante = next((r for r in restaurantes if r.nome == nome), None)
            if restaurante:
                restaurante.criar_cardapio()
                salvar_restaurantes(restaurantes)
            else:
                print("Restaurante não encontrado.")

        elif opcao == "3":
            nome = input("Nome do restaurante: ")
            restaurante = next((r for r in restaurantes if r.nome == nome), None)
            if restaurante:
                restaurante.registrar_vendas()
                salvar_restaurantes(restaurantes)
            else:
                print("Restaurante não encontrado.")

        elif opcao == "4":
            lat = float(input("Latitude: "))
            lon = float(input("Longitude: "))
            localidade = {'lat': lat, 'lon': lon}
            restaurantes_proximos = sorted(restaurantes, key=lambda r: r.verificar_proximidade(localidade))
            for restaurante in restaurantes_proximos:
                print(restaurante.nome)

        elif opcao == "5":
            for restaurante in restaurantes:
                print(restaurante.nome)

        elif opcao == "6":
            nome = input("Nome do restaurante: ")
            restaurantes = [r for r in restaurantes if r.nome != nome]
            salvar_restaurantes(restaurantes)

        elif opcao == "7":
            nome = input("Nome do restaurante: ")
            restaurante = next((r for r in restaurantes if r.nome == nome), None)
            if restaurante:
                n_pedidos = int(input("Número de pedidos: "))
                restaurante.n_pedidos = n_pedidos
                salvar_restaurantes(restaurantes)
            else:
                print("Restaurante não encontrado.")
                
        elif opcao == 8:
            pass

        elif opcao == "9":
            break

        else:
            print("Opção inválida!")