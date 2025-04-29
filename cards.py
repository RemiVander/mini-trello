from utils import load_data, save_data

def add_card(board_name, list_name, card_title):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            for lst in board["lists"]:
                if lst["name"] == list_name:
                    if card_title in lst["cards"]:
                        print(" La carte existe déjà.")
                        return
                    lst["cards"].append(card_title)
                    save_data(data)
                    print(f"Carte '{card_title}' ajoutée à la liste '{list_name}' du board '{board_name}'.")
                    return
            print(" Liste non trouvée.")
            return
    print(" Board non trouvé.")

def delete_card(board_name, list_name, card_title):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            for lst in board["lists"]:
                if lst["name"] == list_name:
                    if card_title in lst["cards"]:
                        lst["cards"].remove(card_title)
                        save_data(data)
                        print(f"🗑️ Carte '{card_title}' supprimée.")
                        return
                    else:
                        print(" Carte non trouvée.")
                        return
            print(" Liste non trouvée.")
            return
    print(" Board non trouvé.")

def move_card(board_name, from_list, to_list, card_title):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            source = next((lst for lst in board["lists"] if lst["name"] == from_list), None)
            target = next((lst for lst in board["lists"] if lst["name"] == to_list), None)
            if not source or not target:
                print(" Liste source ou destination non trouvée.")
                return
            if card_title not in source["cards"]:
                print(" Carte non trouvée dans la liste source.")
                return
            source["cards"].remove(card_title)
            target["cards"].append(card_title)
            save_data(data)
            print(f" Carte déplacée de '{from_list}' vers '{to_list}'.")
            return
    print(" Board non trouvé.")

def list_cards(board_name, list_name):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            for lst in board["lists"]:
                if lst["name"] == list_name:
                    print(f"📋 Cartes dans la liste '{list_name}' :")
                    for card in lst["cards"]:
                        print(f" - {card}")
                    return
            print("Liste non trouvée.")
            return
    print(" Board non trouvé.")
