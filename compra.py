from connect_database import connect_database
from produto import read_table_produto
from usuario import read_table_usuario
from vendedor import read_table_vendedor

driver = connect_database()

def create_constraint_compra():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Compra) REQUIRE c.id IS UNIQUE")

def insert_compra():
    print('Selecione o usuário:\n')
    usuarios = read_table_usuario()
    if not usuarios:
        print('Nenhum usuário encontrado')
        return
    i_usuario = int(input('Índice do usuário: '))
    if i_usuario < 1 or i_usuario > len(usuarios):
        print('Índice inválido')
        return

    print('Selecione o produto:\n')
    produtos = read_table_produto()
    if not produtos:
        print('Nenhum produto encontrado')
        return
    i_produto = int(input('Índice do produto: '))
    if i_produto < 1 or i_produto > len(produtos):
        print('Índice inválido')
        return

    usuario = usuarios[i_usuario - 1]
    produto = produtos[i_produto - 1]

    try:
        frete = float(input("Frete: "))
    except ValueError:
        print("Frete inválido")
        return

    valor = produto["preco"] + frete

    with driver.session() as session:
        session.run(
            """
            MATCH (u:Usuario {id: $usuario_id})
            MATCH (p:Produto {id: $produto_id})
            MATCH (v:Vendedor)-[:POSSUI]->(p)
            CREATE (c:Compra {id: randomUUID(), frete: $frete, valor: $valor})
            CREATE (u)-[:REALIZOU]->(c)
            CREATE (c)-[:CONTEM]->(p)
            CREATE (c)-[:VENDIDO_POR]->(v)
            """,
            usuario_id=usuario["id"], produto_id=produto["id"], frete=frete, valor=valor
        )
    print(f"Compra registrada: {usuario['nome']} comprou {produto['nome']} por R${valor:.2f}")

def read_table_compra():
    with driver.session() as session:
        result = session.run("MATCH (c:Compra) RETURN c")
        rows = [record["c"] for record in result]
    for i, row in enumerate(rows, 1):
        print(f'{i} - {row["usuario_nome"]} comprou {row["produto_nome"]} de {row["vendedor_nome"]} | frete: R${row["frete"]:.2f} | total: R${row["valor"]:.2f} | id: {row["id"]}')
    print('=======================================')
    return rows