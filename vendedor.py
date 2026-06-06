from connect_database import connect_database

driver = connect_database()

def create_constraint_vendedor():
    with driver.session() as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (v:Vendedor) REQUIRE v.id IS UNIQUE")

def insert_vendedor():
    nome = input("Nome: ")
    cnpj = input("CNPJ: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    with driver.session() as session:
        session.run(
            """
            CREATE (v:Vendedor {
                id: randomUUID(),
                nome: $nome,
                cnpj: $cnpj,
                email: $email,
                senha: $senha,
                cep: $cep,
                cidade: $cidade,
                estado: $estado,
                rua: $rua,
                numero: $numero
            })
            """,
            nome=nome, cnpj=cnpj, email=email, senha=senha,
            cep=cep, cidade=cidade, estado=estado, rua=rua, numero=numero
        )
    print(f"Vendedor '{nome}' inserido com sucesso.")

def read_table_vendedor():
    with driver.session() as session:
        result = session.run("MATCH (v:Vendedor) RETURN v")
        rows = [record["v"] for record in result]
    for i, row in enumerate(rows, 1):
        print(f'{i} - nome: {row["nome"]} | cnpj: {row["cnpj"]} | email: {row["email"]} | cidade: {row["cidade"]} | id: {row["id"]}')
    print('=======================================')
    return rows