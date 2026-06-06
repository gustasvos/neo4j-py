from connect_database import connect_database

driver = connect_database()

def create_constraint_usuario():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (u:Usuario) REQUIRE u.id IS UNIQUE")

def insert_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("CPF: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    cartao = input("Cartão: ")
    with driver.session() as session:
        session.run(
            """
            CREATE (u:Usuario {
                id: randomUUID(),
                nome: $nome,
                email: $email,
                senha: $senha,
                cpf: $cpf,
                cep: $cep,
                cidade: $cidade,
                estado: $estado,
                rua: $rua,
                numero: $numero,
                cartao: $cartao
            })
            """,
            nome=nome, email=email, senha=senha, cpf=cpf,
            cep=cep, cidade=cidade, estado=estado,
            rua=rua, numero=numero, cartao=cartao
        )
    print(f"Usuário '{nome}' inserido com sucesso.")

def read_table_usuario():
    with driver.session() as session:
        result = session.run("MATCH (u:Usuario) RETURN u")
        rows = [record["u"] for record in result]
    for i, row in enumerate(rows, 1):
        print(f'{i} - id: {row["id"]} | nome: {row["nome"]} | email: {row["email"]} | cpf: {row["cpf"]} | cidade: {row["cidade"]}')
    print('=======================================')
    return rows