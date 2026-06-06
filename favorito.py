from connect_database import connect_database
from produto import read_table_produto
from usuario import read_table_usuario

driver = connect_database()

def create_constraint_favorito():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (f:Favorito) REQUIRE f.id IS UNIQUE")

def insert_favorito():
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

    with driver.session() as session:
        session.run(
            """
            CREATE (f:Favorito {
                id: randomUUID(),
                usuario_id: $usuario_id,
                produto_id: $produto_id,
                usuario_nome: $usuario_nome,
                produto_nome: $produto_nome,
                produto_descricao: $produto_descricao,
                produto_preco: $produto_preco
            })
            """,
            usuario_id=usuario["id"], produto_id=produto["id"],
            usuario_nome=usuario["nome"], produto_nome=produto["nome"],
            produto_descricao=produto["descricao"], produto_preco=produto["preco"]
        )
    print(f"Favorito adicionado: {usuario['nome']} -> {produto['nome']}")

def read_table_favorito():
    with driver.session() as session:
        result = session.run("MATCH (f:Favorito) RETURN f")
        rows = [record["f"] for record in result]
    for i, row in enumerate(rows, 1):
        print(f'{i} - {row["usuario_nome"]} -> {row["produto_nome"]} | descrição: {row["produto_descricao"]} | preço: R${row["produto_preco"]:.2f} | id: {row["id"]}')
    print('=======================================')
    return rows