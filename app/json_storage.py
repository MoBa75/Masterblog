import json
from json import JSONDecodeError


def get_data():
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        with open('data/data.json', 'w') as file:
            file.write('[]')
            return []


def save_data(posts):
    if not posts or not isinstance(posts, list):
        raise TypeError("Error: Save element needs to be list!")
    # ensuring date format is valid
    for post in posts:
        if not post or not isinstance(post, dict):
            raise TypeError("Error: Each element needs to be dictionary!")
        if not len(post) == 4:
            raise KeyError("Error: 'id', 'author', 'title', 'content' need to exist!")
        for key in post:
            if key not in ['id', 'author', 'title', 'content']:
                raise KeyError(f"Error: Wrong key '{key}'!")
    with open('data/data.json', 'w') as file:
        file.write(json.dumps(posts, indent=4))


def create_data(new_post):
    if not new_post or not isinstance(new_post, dict):
        raise TypeError("Error: Save element needs to be dictionary!")
    if not len(new_post) == 4:
        raise KeyError("Error: 'id', 'author', 'title', 'content' need to exist!")
    for key in new_post:
        if key not in ['id', 'author', 'title', 'content']:
            raise KeyError(f"Error: Wrong key '{key}'!")
    posts = get_data()
    posts.append(new_post)
    save_data(posts)


def delete_data(post_index):
    if not isinstance(post_index, int):
        raise TypeError("Error: Delete index needs to be integer!")
    if post_index <= 0:
        raise ValueError("Error: Delete index must be a positiv numer!")
    posts = get_data()
    if post_index > len(posts):
        raise ValueError("Error: Delete index exceeds data length!")
    posts.pop(post_index)
    save_data(posts)


def update_data(updated_post):
    if not updated_post or not isinstance(updated_post, dict):
        raise TypeError("Error: Update element needs to be dictionary!")
    if not len(updated_post) == 4:
        raise KeyError("Error: 'id', 'author', 'title', 'content' need to exist!")
    for key in updated_post:
        if key not in ['id', 'author', 'title', 'content']:
            raise KeyError(f"Error: Wrong key '{key}'!")
    posts = get_data()
    for index, post in enumerate(posts):
        if post['id'] == updated_post['id']:
            posts[index] = updated_post
            save_data(posts)
