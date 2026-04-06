from ordens import PosOrdem, InOrden, PreOrdem
from models.avl_tree import AVLTree

avl_tree = AVLTree()

while True:
    print("\nMenu:")
    print("1. Inserir valor")
    print("2. Buscar valor")
    print("3. Excluir valor")
    print("4. Exibir em pré-ordem")
    print("5. Exibir em pós-ordem")
    print("6. Exibir em ordem")
    print("7. Sair")

    choice = input("\nEscolha uma opção: \n")

    if choice == '1':
        value = int(input("Digite o valor a ser inserido: "))
        avl_tree.insert(value)
        print("\n--- Estado da Árvore após Inserção ---")
        avl_tree.print_tree()
        print("--------------------------------------\n")
    elif choice == '2':
        print("\n")
        value = int(input("Digite o valor a ser buscado: "))
        result = avl_tree.search(value)
        if result:
            print(f"Valor {value} encontrado na árvore.")
        else:
            print(f"Valor {value} não encontrado na árvore.")
        print("\n")
    elif choice == '3':
        value = int(input("Digite o valor a ser removido: "))
        avl_tree.delete(value)
        print("\n--- Estado da Árvore após Remoção ---")
        avl_tree.print_tree()
        print("--------------------------------------\n")
    elif choice == '4':
        print("\n")
        print("Árvore em pré-ordem:")
        pre_order = PreOrdem()
        pre_order.pre_ordem(avl_tree.root)
        print("\n")
    elif choice == '5':
        print("\n")
        print("Árvore em pós-ordem:")
        post_order = PosOrdem()
        post_order.post_order(avl_tree.root)
        print("\n")
    elif choice == '6':
        print("\n")
        print("Árvore em ordem:")
        in_order = InOrden()
        in_order.in_orden(avl_tree.root)
        print("\n")
    elif choice == '7':
        print("\n")
        print("Saindo...")
        break