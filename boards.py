from utils import load_data, save_data

def create_board(name):
    data = load_data()
    if any(board["name"] == name for board in data["boards"]):
        print(f" Le board '{name}' existe déjà.")
        return
    data["boards"].append({"name": name, "lists": []})
    save_data(data)
    print(f" Board '{name}' créé.")

def delete_board(name):
    data = load_data()
    original_len = len(data["boards"])
    data["boards"] = [board for board in data["boards"] if board["name"] != name]
    if len(data["boards"]) == original_len:
        print(f" Board '{name}' introuvable.")
    else:
        save_data(data)
        print(f" Board '{name}' supprimé.")

def list_boards():
    data = load_data()
    boards = data.get("boards", [])
    if not boards:
        print("📭 Aucun board disponible.")
        return
    print(" Boards existants :")
    for board in boards:
        print(f" - {board['name']}")
