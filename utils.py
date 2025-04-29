import json

def load_data(filename='data.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
