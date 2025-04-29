from boards import create_board, delete_board, list_boards
from lists import add_list, delete_list, list_lists
from cards import add_card, delete_card, move_card, list_cards

def main_menu():
    while True:
        print("\n=== Mini-Trello ===")
        print("1. Gérer les boards")
        print("2. Gérer les listes")
        print("3. Gérer les cartes")
        print("0. Quitter")
        choice = input("Choix : ")
        
        if choice == "1":
            board_menu()
        elif choice == "2":
            list_menu()
        elif choice == "3":
            card_menu()
        elif choice == "0":
            print("👋 À bientôt !")
            break
        else:
            print(" Choix invalide.")

def board_menu():
    print("\n--- Gestion des boards ---")
    print("1. Créer un board")
    print("2. Supprimer un board")
    print("3. Lister les boards")
    choice = input("Choix : ")

    if choice == "1":
        name = input("Nom du board : ")
        create_board(name)
    elif choice == "2":
        name = input("Nom du board à supprimer : ")
        delete_board(name)
    elif choice == "3":
        list_boards()
    else:
        print(" Choix invalide.")

def list_menu():
    print("\n--- Gestion des listes ---")
    print("1. Ajouter une liste")
    print("2. Supprimer une liste")
    print("3. Lister les listes d’un board")
    choice = input("Choix : ")

    if choice == "1":
        board = input("Nom du board : ")
        list_name = input("Nom de la nouvelle liste : ")
        add_list(board, list_name)
    elif choice == "2":
        board = input("Nom du board : ")
        list_name = input("Nom de la liste à supprimer : ")
        delete_list(board, list_name)
    elif choice == "3":
        board = input("Nom du board : ")
        list_lists(board)
    else:
        print(" Choix invalide.")

def card_menu():
    print("\n--- Gestion des cartes ---")
    print("1. Ajouter une carte")
    print("2. Supprimer une carte")
    print("3. Déplacer une carte")
    print("4. Lister les cartes d’une liste")
    choice = input("Choix : ")

    if choice == "1":
        board = input("Nom du board : ")
        list_name = input("Nom de la liste : ")
        card_title = input("Titre de la carte : ")
        add_card(board, list_name, card_title)
    elif choice == "2":
        board = input("Nom du board : ")
        list_name = input("Nom de la liste : ")
        card_title = input("Titre de la carte à supprimer : ")
        delete_card(board, list_name, card_title)
    elif choice == "3":
        board = input("Nom du board : ")
        from_list = input("Liste source : ")
        to_list = input("Liste cible : ")
        card_title = input("Titre de la carte : ")
        move_card(board, from_list, to_list, card_title)
    elif choice == "4":
        board = input("Nom du board : ")
        list_name = input("Nom de la liste : ")
        list_cards(board, list_name)
    else:
        print(" Choix invalide.")

if __name__ == "__main__":
    main_menu()
