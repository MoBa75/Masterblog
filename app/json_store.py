import json
from json import JSONDecodeError


def get_data():
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        with open('data.json', 'w') as file:
            file.write('{}')
            return {}


"""def save_data(xxx):
    with open('/data/data.json', 'w') as file:
        file.write(json.dumps(xxx, indent=4))"""