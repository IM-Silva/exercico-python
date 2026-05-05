carrinho = []
print(" ___ Carrinho de Compras ___ ")
while True:
    print(" [1] Adicionar produto")
    print(" [2] Ver Carrinho")
    print(" [3] Finalizar Compra")
    alternativa=int(input("  Digite uma das opções acima:  "))
    if alternativa == 1:
        nome_produto=input("Nome do Produto: ")
        valor_produto=float(input(" Qual o preço do produto: "))
        produto = {
            "nome_produto":nome_produto,
            "valor_produto":valor_produto
        }
        carrinho.append(produto)
    elif alternativa == 2:
        if carrinho == []:
            print("Carrinho Vazio")
        else:
            for item in carrinho:
                print(item["nome_produto"])
                print(item["valor_produto"])
    elif alternativa == 3:
        if carrinho == []:
            print(" ___ Nenhum Produto foi adicionado ao carrinho ___")
        else:
            total = 0
            for item in carrinho:
                total = total + item["valor_produto"]
                print(f' ___ Produto adicionado: {item["nome_produto"]} ___')
                print(f' ___ Valor do produto: R${item["valor_produto"]:.2f} ___')
            print(f" ___ Valor total: R${total:.2f} ___")
        break
    else:
        print(" ___ Opção Inválida! ___")
