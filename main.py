from produto import create_constraint_produto, insert_produto, read_table_produto
from usuario import create_constraint_usuario, insert_usuario, read_table_usuario
from vendedor import create_constraint_vendedor, insert_vendedor, read_table_vendedor
from compra import create_constraint_compra, insert_compra, read_table_compra
from favorito import create_constraint_favorito, insert_favorito, read_table_favorito

acoes_crud = {
    "Usuario":  (insert_usuario,  read_table_usuario),
    "Produto":  (insert_produto,  read_table_produto),
    "Vendedor": (insert_vendedor, read_table_vendedor),
    "Compras":  (insert_compra,   read_table_compra),
    "Favoritos":(insert_favorito, read_table_favorito),
}

def menu_crud(col):
    create, read = acoes_crud[col]
    while True:
        print(f"\n{col.upper()}")
        print(f"1. Criar {col}")
        print(f"2. Ler {col}")
        # print(f"3. Atualizar {col}")
        # if update:
            # print(f"4. Deletar {col}")
        # else:
            # print(f"3. Deletar {col}")
        print(f"0. Voltar")
        option = int(input("Escolha uma opção: "))
        if option == 1:
            create()
        elif option == 2:
            read()
        # elif option == 3:
            # if update:
            # update()
            # else:
            #     if delete:
            #         delete()
            #     else:
            #         print("Opção inválida")
        # elif option == 4 and update:
        #     delete()
        elif option == 0:
            break
        else:
            print("Opção inválida")

def menu_neo4j():
    while True:
        print("MENU\n")
        print("ESCOLHA A TABELA PARA REALIZAR AS AÇÕES CRUD:\n")
        print("1. Usuario")
        print("2. Produto")
        print("3. Vendedor")
        print("4. Compras")
        print("5. Favoritos")
        print("0. Sair")
        option = int(input("Escolha uma opção: "))
        if option == 1:
            create_constraint_usuario()
            menu_crud("Usuario")
        elif option == 2:
            create_constraint_produto()
            menu_crud("Produto")
        elif option == 3:
            create_constraint_vendedor()
            menu_crud("Vendedor")
        elif option == 4:
            create_constraint_compra()
            menu_crud("Compras")
        elif option == 5:
            create_constraint_favorito()
            menu_crud("Favoritos")
        elif option == 0:
            print("Saindo.")
            break
        else:
            print("Opção inválida")

menu_neo4j()