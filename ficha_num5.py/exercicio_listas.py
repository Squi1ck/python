
# Lista vazia para guardar os produtos
products = []


# 3. Função para adicionar um produto
def add(product, price, tax):
    produto = {
        "product": product,
        "price": price,
        "tax": tax
    }

    products.append(produto)
    print("Produto adicionado com sucesso!")


# 4. Função para atualizar o preço final
def update_final_price(produto):
    produto["final_price"] = round(
        produto["price"] * (1 + produto["tax"]), 2
    )


# 5. Função para imprimir os dados de um produto
def print_product(nome):
    encontrado = False

    for produto in products:
        if produto["product"].lower() == nome.lower():

            # Atualizar o preço final antes de imprimir
            update_final_price(produto)

            print("\n--- Dados do Produto ---")
            print("Produto:", produto["product"])
            print("Preço:", produto["price"])
            print("IVA:", produto["tax"])
            print("Preço final:", f'{produto["final_price"]:.2f} €')

            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado!")


# 7. Menu principal
while True:

    print("\n===== MENU PRODUTOS =====")
    print("1 - Inserir novo produto")
    print("2 - Listar produtos existentes")
    print("3 - Atualizar preço final de todos os produtos")
    print("4 - Imprimir dados de um produto específico")
    print("5 - Terminar aplicação")

    opcao = input("Escolha uma opção: ")

    # Opção 1 - Inserir produto
    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        iva = float(input("IVA (ex: 0.23 para 23%): "))

        add(nome, preco, iva)

    # Opção 2 - Listar produtos
    elif opcao == "2":
        if len(products) == 0:
            print("Não existem produtos registados!")
        else:
            print("\n--- Lista de Produtos ---")

            for produto in products:
                print(produto["product"], "-", produto["price"], "€")

    # Opção 3 - Atualizar preços finais
    elif opcao == "3":
        if len(products) == 0:
            print("Não existem produtos para atualizar!")
        else:
            for produto in products:
                update_final_price(produto)

            print("Preços finais atualizados com sucesso!")

    # Opção 4 - Imprimir produto específico
    elif opcao == "4":
        nome = input("Introduza o nome do produto: ")
        print_product(nome)

    # Opção 5 - Terminar aplicação
    elif opcao == "5":
        print("Aplicação terminada!")
        break

    else:
        print("Opção inválida! Tente novamente.")
