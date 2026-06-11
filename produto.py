from connect_database import connect_database
from vendedor import read_table_vendedor

driver = connect_database()

def create_constraint_produto():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Produto) REQUIRE p.id IS UNIQUE")

def insert_produto():
    print('Selecione o vendedor:\n')
    vendedores = read_table_vendedor()
    if not vendedores:
        print("Nenhum vendedor encontrado. Primeiro crie um vendedor para depois criar um produto.")
        return
    i_vendedor = int(input('Índice do vendedor: '))
    if i_vendedor < 1 or i_vendedor > len(vendedores):
        print('Índice inválido')
        return

    vendedor = vendedores[i_vendedor - 1]
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido")
        return
    with driver.session() as session:
        session.run(
            """
            MATCH (v:Vendedor {id: $vendedor_id})
            CREATE (p:Produto {id: randomUUID(), nome: $nome, descricao: $descricao, preco: $preco})
            CREATE (v)-[:POSSUI]->(p)
            """,
            nome=nome, descricao=descricao, preco=preco, vendedor_id=vendedor["id"]
        )
    print(f"Produto '{nome}' inserido com sucesso.")

def read_table_produto():
    with driver.session() as session:
        result = session.run("MATCH (p:Produto) RETURN p")
        rows = [record["p"] for record in result]
    for i, row in enumerate(rows, 1):
        print(f'{i} - nome: {row["nome"]} | descrição: {row["descricao"]} | preço: R${row["preco"]:.2f} | id: {row["id"]}')
    print('=======================================')
    return rows