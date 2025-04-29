from utils import load_data, save_data

def add_list(board_name, list_name):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            if any(lst["name"] == list_name for lst in board["lists"]):
                print(f" La liste '{list_name}' existe déjà dans le board '{board_name}'.")
                return
            board["lists"].append({"name": list_name, "cards": []})
            save_data(data)
            print(f" Liste '{list_name}' ajoutée au board '{board_name}'.")
            return
    print(f" Board '{board_name}' introuvable.")

def delete_list(board_name, list_name):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            original_len = len(board["lists"])
            board["lists"] = [lst for lst in board["lists"] if lst["name"] != list_name]
            if len(board["lists"]) == original_len:
                print(f" Liste '{list_name}' introuvable.")
            else:
                save_data(data)
                print(f"🗑️ Liste '{list_name}' supprimée du board '{board_name}'.")
            return
    print(f" Board '{board_name}' introuvable.")

def list_lists(board_name):
    data = load_data()
    for board in data["boards"]:
        if board["name"] == board_name:
            if not board["lists"]:
                print(f"📭 Aucune liste dans le board '{board_name}'.")
                return
            print(f" Listes dans le board '{board_name}' :")
            for lst in board["lists"]:
                print(f" - {lst['name']}")
            return
    print(f" Board '{board_name}' introuvable.")
