import json
from json import JSONDecodeError


def get_data():
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        with open('data/data.json', 'w') as file:
            file.write('{}')
            return {}


def save_data(new_post):
    if not new_post or not isinstance(new_post, dict):
        raise TypeError("Error: Save element needs to be dictionary!")
    if not len(new_post) == 4:
        raise KeyError("Error: 'id', 'author', 'title', 'content' need to exist!")
    for key in new_post:
        if key not in ['id', 'author', 'title', 'content']:
            raise KeyError(f"Error: Wrong key '{key}'!")
    posts = get_data()
    posts.append(new_post)
    with open('data/data.json', 'w') as file:
        file.write(json.dumps(posts, indent=4))
