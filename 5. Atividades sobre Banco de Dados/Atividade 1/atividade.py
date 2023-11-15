from biblioteca import *

while True:
    print("\nEscolha uma operação:")
    print("1. Visualizar dados")
    print("2. Manipular dados (Inserir, Atualizar, Excluir)")
    print("3. Criar/Excluir/Atualizar Tabela")
    print("0. Sair")

    escolha_menu = input("Digite o número da operação desejada: ")

    if escolha_menu == "0":
        break
    elif escolha_menu == "1":
        tabelas_disponiveis = obter_tabelas()
        print("\nEscolha uma tabela para visualizar:")
        for i, tabela in enumerate(tabelas_disponiveis, 1):
            print(f"{i}. {tabela}")

        escolha_tabela = input("Digite o número da tabela desejada: ")

        if escolha_tabela.isdigit() and 1 <= int(escolha_tabela) <= len(tabelas_disponiveis):
            tabela_escolhida = tabelas_disponiveis[int(escolha_tabela) - 1]
            visualizar_dados(tabela_escolhida)
        else:
            print("Opção inválida. Tente novamente.")
    elif escolha_menu == "2":
        tabelas_disponiveis = obter_tabelas()
        print("\nEscolha uma tabela para manipular:")
        for i, tabela in enumerate(tabelas_disponiveis, 1):
            print(f"{i}. {tabela}")

        escolha_tabela = input("Digite o número da tabela desejada: ")

        if escolha_tabela.isdigit() and 1 <= int(escolha_tabela) <= len(tabelas_disponiveis):
            tabela_escolhida = tabelas_disponiveis[int(escolha_tabela) - 1]

            print("\nEscolha uma operação:")
            print("1. Inserir dados")
            print("2. Atualizar dados")
            print("3. Excluir dados")

            escolha_operacao = input("Digite o número da operação desejada: ")

            if escolha_operacao == "1":
                campos_tabela = obter_campos(tabela_escolhida)
                inserir_dados(tabela_escolhida, campos_tabela)
            elif escolha_operacao == "2":
                atualizar_dados(tabela_escolhida)
            elif escolha_operacao == "3":
                excluir_dados(tabela_escolhida)
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")
    elif escolha_menu == "3":
        print("\nEscolha uma operação:")
        print("1. Criar tabela")
        print("2. Excluir tabela")
        print("3. Atualizar nome da tabela")

        escolha_operacao_tabela = input("Digite o número da operação desejada: ")

        if escolha_operacao_tabela == "1":
            criar_tabela()
        elif escolha_operacao_tabela == "2":
            excluir_tabela()
        elif escolha_operacao_tabela == "3":
            atualizar_nome_tabela()
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
