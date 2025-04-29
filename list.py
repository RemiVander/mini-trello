# Le projet suiavnt consiste à développer un mini-Trello en ligne de commande, entièrement basé sur des fonctions et sans recours à la POO,
# afin de familiariser un groupe de trois apprenants Python avec un véritable workflow Git (Git Flow).
# Les données seront stockées dans un unique fichier JSON (data.json) : on y gère des « boards »,
# chaque board contenant plusieurs « lists » (colonnes) et chaque list une collection de « cards » (éléments).
# Les apprenants travailleront en parallèle sur trois modules distincts :

# Boards (création, suppression, listing)
# Lists (ajout, suppression, listing au sein d’un board)
# Cards (ajout, suppression, déplacement entre lists, listing)

# Chaque module est développé dans une branche feature/..., puis fusionné dans develop après revue de code par un pair.

from board import list_boards, add_board, remove_board

def list_lists(board):
    """
    Affiche la liste des listes d'un tableau donné.

    Args:
        board (dict): Le tableau dont on veut afficher les listes.
    """
    if not board["lists"]:
        print("Aucune liste dans ce tableau.")
        return

    print(f"Listes dans le tableau '{board['name']}':")
    for i, list_ in enumerate(board["lists"], start=1):
        print(f"{i}. {list_['name']}")


def add_list(board, list_name):
    """
    Ajoute une nouvelle liste à un tableau donné.

    Args:
        board (dict): Le tableau auquel on veut ajouter une liste.
        list_name (str): Le nom de la nouvelle liste.
    """
    new_list = {"name": list_name, "cards": []}
    board["lists"].append(new_list)
    print(f"Liste '{list_name}' ajoutée au tableau '{board['name']}'.")


def remove_list(board, list_index):
    """
    Supprime une liste d'un tableau donné.

    Args:
        board (dict): Le tableau dont on veut supprimer une liste.
        list_index (int): L'index de la liste à supprimer.
    """
    if list_index < 0 or list_index >= len(board["lists"]):
        print("Index de liste invalide.")
        return

    removed_list = board["lists"].pop(list_index)
    print(f"Liste '{removed_list['name']}' supprimée du tableau '{board['name']}'.")



    