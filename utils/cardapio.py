def criar_cardapio(self):
    print("Digite os itens do cardápio (digite 'sair' para terminar):")
    while True:
        nome_item = input("Nome do item: ")
        if nome_item.lower() == 'sair':
            break

        tipo_item = input("Tipo do item (comida ou bebida): ").lower()
        if tipo_item == 'bebida':
            alcoolica = input("A bebida é alcoólica? (sim ou não): ").lower()
            item = {'nome': nome_item, 'tipo': tipo_item, 'alcoolica': alcoolica == 'sim'}
        else:
            item = {'nome': nome_item, 'tipo': tipo_item}

        self.cardapio.append(item)
        print("Item adicionado ao cardápio com sucesso!")
