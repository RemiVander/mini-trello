# Le projet suiavnt consiste à développer un mini-Trello en ligne de commande, entièrement basé sur des fonctions et sans recours à la POO,
# afin de familiariser un groupe de trois apprenants Python avec un véritable workflow Git (Git Flow).
# Les données seront stockées dans un unique fichier JSON (data.json) : on y gère des « boards »,
# chaque board contenant plusieurs « lists » (colonnes) et chaque list une collection de « cards » (éléments).
# Les apprenants travailleront en parallèle sur trois modules distincts :

# Boards (création, suppression, listing)
# Lists (ajout, suppression, listing au sein d’un board)
# Cards (ajout, suppression, déplacement entre lists, listing)

# Chaque module est développé dans une branche feature/..., puis fusionné dans develop après revue de code par un pair.


def list_boards(boards):
    """
    Affiche la liste des tableaux disponibles.

    Args:
        boards (list): La liste des tableaux.
    """
    if not boards:
        print("Aucun tableau disponible.")
        return

    print("Tableaux disponibles :")
    for i, board in enumerate(boards, start=1):
        print(f"{i}. {board['name']}")


def add_board(boards, board_name):
    """
    Ajoute un nouveau tableau à la liste des tableaux.

    Args:
        boards (list): La liste des tableaux.
        board_name (str): Le nom du nouveau tableau.
    """
    new_board = {"name": board_name, "lists": []}
    boards.append(new_board)
    print(f"Tableau '{board_name}' ajouté.")


def remove_board(boards, board_index):
    """
    Supprime un tableau de la liste des tableaux.
    Args:
        boards (list): La liste des tableaux.
        board_index (int): L'index du tableau à supprimer.
    """
    if board_index < 0 or board_index >= len(boards):
        print("Index de tableau invalide.")
        return

    removed_board = boards.pop(board_index)
    print(f"Tableau '{removed_board['name']}' supprimé.")
