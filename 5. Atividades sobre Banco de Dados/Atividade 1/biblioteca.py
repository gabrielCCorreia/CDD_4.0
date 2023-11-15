import mysql.connector
from prettytable import PrettyTable

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academia"
)

cursor = banco.cursor()


def obter_tabelas():
    query = "SHOW TABLES"
    cursor.execute(query)
    return [tabela[0] for tabela in cursor.fetchall()]


def obter_campos(tabela):
    query = f"DESCRIBE {tabela}"
    cursor.execute(query)
    return [campo[0] for campo in cursor.fetchall()]


def criar_tabela():
    nome_tabela = input("Digite o nome da nova tabela: ")
    num_campos = int(input("Digite o número de campos na tabela: "))

    campos = []
    for x in range(num_campos):
        nome_campo = input(f"Digite o nome do {x + 1}° campo: ")
        tipo_campo = input(f"Digite o tipo do {x + 1}° campo: ")
        campos.append(f"{nome_campo} {tipo_campo}")

    query = f"CREATE TABLE {nome_tabela} ({', '.join(campos)})"
    cursor.execute(query)
    banco.commit()
    print(f"Tabela {nome_tabela} criada com sucesso!")


def excluir_tabela():
    tabelas_disponiveis = obter_tabelas()
    print("\nEscolha uma tabela para excluir:")
    for i, tabela in enumerate(tabelas_disponiveis, 1):
        print(f"{i}. {tabela}")

    escolha_tabela = input("Digite o número da tabela desejada: ")

    if escolha_tabela.isdigit() and 1 <= int(escolha_tabela) <= len(tabelas_disponiveis):
        tabela_escolhida = tabelas_disponiveis[int(escolha_tabela) - 1]

        query = f"DROP TABLE {tabela_escolhida}"
        cursor.execute(query)
        banco.commit()
        print(f"Tabela {tabela_escolhida} excluída com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")


def atualizar_nome_tabela():
    tabelas_disponiveis = obter_tabelas()
    print("\nEscolha uma tabela para atualizar o nome:")
    for i, tabela in enumerate(tabelas_disponiveis, 1):
        print(f"{i}. {tabela}")

    escolha_tabela = input("Digite o número da tabela desejada: ")

    if escolha_tabela.isdigit() and 1 <= int(escolha_tabela) <= len(tabelas_disponiveis):
        tabela_antiga = tabelas_disponiveis[int(escolha_tabela) - 1]
        novo_nome = input("Digite o novo nome para a tabela: ")

        query = f"ALTER TABLE {tabela_antiga} RENAME TO {novo_nome}"
        cursor.execute(query)
        banco.commit()
        print(f"Nome da tabela atualizado para {novo_nome} com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")


def inserir_dados(tabela, campos):
    valores = []
    for campo in campos:
        valor = input(f"Digite o valor para {campo}: ")
        valores.append(valor)

    campos_str = ', '.join(campos)
    placeholders = ', '.join(['%s'] * len(campos))

    query = f"INSERT INTO {tabela} ({campos_str}) VALUES ({placeholders})"
    cursor.execute(query, tuple(valores))
    banco.commit()
    print(f"Dados inseridos na tabela {tabela} com sucesso!")


def visualizar_dados(tabela):
    query = f"SELECT * FROM {tabela}"
    cursor.execute(query)
    resultados = cursor.fetchall()

    campos_tabela = obter_campos(tabela)

    tabela_bonita = PrettyTable(campos_tabela)

    for resultado in resultados:
        tabela_bonita.add_row(resultado)

    print(tabela_bonita)


def atualizar_dados(tabela):
    campos_tabela = obter_campos(tabela)

    print("\nCampos disponíveis para atualização:")
    for i, campo in enumerate(campos_tabela, 1):
        print(f"{i}. {campo}")

    escolha_campo = input("Escolha o número do campo que deseja atualizar: ")

    if escolha_campo.isdigit() and 1 <= int(escolha_campo) <= len(campos_tabela):
        campo_escolhido = campos_tabela[int(escolha_campo) - 1]
        novo_valor = input(f"Digite o novo valor para {campo_escolhido}: ")

        campo_id = input("Digite o valor do campo identificador para localizar a linha a ser atualizada: ")

        query = f"UPDATE {tabela} SET {campo_escolhido} = %s WHERE {campos_tabela[0]} = %s"
        cursor.execute(query, (novo_valor, campo_id))
        banco.commit()
        print(f"Dados atualizados na tabela {tabela} com sucesso!")
    else:
        print("Opção inválida. Tente novamente.")


def excluir_dados(tabela):
    campo_id = obter_campos(tabela)[0]

    valor_id = input(f"Digite o valor do campo {campo_id} para excluir a linha: ")

    query = f"DELETE FROM {tabela} WHERE {campo_id} = %s"
    cursor.execute(query, (valor_id,))
    banco.commit()
    print(f"Linha excluída da tabela {tabela} com sucesso!")
