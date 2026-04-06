print("--- Sistema de Pesquisa de Mercado ---")

# --- 1º MENU: ESCOLHA DA OPERAÇÃO ---
print("\nO que você deseja fazer?")
print("1 - Sugestão de Venda")
print("2 - Sugestão de Compra")
print("0 - Sair do Sistema")
opcao_servico = input("Escolha uma opção: ")

# Verificação de Saída
if opcao_servico == "0":
    print("\nSaindo do sistema com sucesso... Até logo!")
else:
    # --- 2º MENU: ESCOLHA DO PRODUTO ---
    print("\nSelecione o produto para a operação:")
    print("1 - Produto 1")
    print("2 - Produto 2")
    print("3 - Produto 3")
    print("4 - Produto 4")
    print("5 - Produto 5")
    opcao_produto = input("Digite o numero do produto (1-5): ")

    # Definindo o nome do produto baseado na escolha
    if opcao_produto == "1":
        nome_produto = "Produto 1"
    elif opcao_produto == "2":
        nome_produto = "Produto 2"
    elif opcao_produto == "3":
        nome_produto = "Produto 3"
    elif opcao_produto == "4":
        nome_produto = "Produto 4"
    elif opcao_produto == "5":
        nome_produto = "Produto 5"
    else:
        nome_produto = "Produto Desconhecido"

    # --- 3º COLETA DE DADOS DOS CONCORRENTES ---
    qtd_texto = input(f"\nQuantos concorrentes você deseja consultar para {nome_produto}? ")
    total = int(qtd_texto)
    

    preco_dos_concorrentes = [0] * total
    soma = 0
    maior = 0
    menor = 0

    for i in range(total):
        valor_input = input(f"Digite o preço do concorrente {i+1}: ").replace(',', '.')
       
        preco = float(valor_input)
        preco_dos_concorrentes[i] = preco
        soma = soma + preco
       
        if i == 0:
            maior = preco
            menor = preco
        else:
            if preco > maior:
                maior = preco
            if preco < menor:
                menor = preco

    media = soma / total

    # --- EXIBIÇÃO DOS RESULTADOS E CÁLCULOS FINAIS ---
    print("\n--- RESULTADOS DA PESQUISA ---")
    print(f"Produto selecionado: {nome_produto}")
    print(f"Média de mercado: R$ {media:.2f}")
    print(f"Maior preço: R$ {maior:.2f}")
    print(f"Menor preço: R$ {menor:.2f}")

    if opcao_servico == "1":
        print(f"\n--- Formação de Preço de Venda ({nome_produto}) ---")
        custo = float(input("Informe o valor de compra (R$): ").replace(',', '.'))
        margem = float(input("Margem de lucro desejada (%): ").replace(',', '.'))

        sugerido = custo * (1 + margem / 100)
        print(f"\n-- VALOR SUGERIDO PARA VENDA --: R$ {sugerido:.2f}")

        if sugerido > maior:
            print("Status: Seu preço está acima de todos os concorrentes.")
        elif sugerido < menor:
            print("Status: Seu preço está abaixo de todos os concorrentes.")
        else:
            print("Status: Seu preço está competitivo.")

    elif opcao_servico == "2":
        print(f"\n--- Sugestão de Custo de Compra ({nome_produto}) ---")
        margem = float(input("Qual margem de lucro você pretende ter ao revender (%): ").replace(',', '.'))
       
        custo_maximo = media / (1 + margem / 100)
       
        print(f"\nPara manter a competitividade com a média (R$ {media:.2f}):")
        print(f"-- CUSTO MÁXIMO SUGERIDO PARA COMPRA --: R$ {custo_maximo:.2f}")

    else:
        print("\nOpção de operação inválida! Reinicie o programa.")