def read_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return data

def write_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)