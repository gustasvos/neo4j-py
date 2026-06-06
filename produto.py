from connect_database import connect_database

driver = connect_database()

def create_constraint_produto():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (p:Produto) REQUIRE p.id IS UNIQUE")

def insert_produto():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido")
        return
    with driver.session() as session:
        session.run(
            "CREATE (p:Produto {id: randomUUID(), nome: $nome, descricao: $descricao, preco: $preco})",
            nome=nome, descricao=descricao, preco=preco
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