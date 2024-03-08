import json

def read_file():
    contents = json.load(open('pieces.json'))
    return contents

def write_file(content):
    json.dump(content, open("pieces.json", "w"), indent=6)

if __name__ == "__main__":
    pass
