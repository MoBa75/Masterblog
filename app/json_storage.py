import json
from json import JSONDecodeError
from app.app_operation import post_validation


def get_posts():
    """
    Reads the saved blog entries from a JSON file and returns the content.
    If the storage file is empty, a new list is created to store the blogs.
    :return: Existing blog entries as a list or empty list.
    """
    try:
        with open('data/data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        with open('data/data.json', 'w') as file:
            file.write('[]')
            return []


def save_data(posts):
    """
    Saves blog entries to the JSON storage file.
    :param posts: Entire blog entries as a list of dictionaries.
    """
    if not posts or not isinstance(posts, list):
        raise TypeError("Error: Save element needs to be list!")
    # ensuring date format is valid
    for post in posts:
        try:
            post_validation(post)
        except (TypeError, KeyError) as error:
            return {'error': error}
    with open('data/data.json', 'w') as file:
        json.dump(posts, file, indent=4)


def save_post(new_post):
    """
    Adds a new blog entry to the existing list
    of blog entries and submits it for saving.
    :param new_post:New blog entry as dictionary
    """
    try:
        new_post = post_validation(new_post)
    except (TypeError, KeyError) as error:
        return {'error': error}
    posts = get_posts()
    posts.append(new_post)
    save_data(posts)


def delete_post(post_index):
    """
    Deletes the selected blog entry from the list of all entries.
    :param post_index: Index of the entry to be deleted as integer.
    """
    if not isinstance(post_index, int):
        raise TypeError("Error: Delete index needs to be integer!")
    if post_index < 0:
        raise ValueError("Error: Delete index must be a positiv numer!")
    posts = get_posts()
    if post_index > len(posts):
        raise ValueError("Error: Delete index exceeds data length!")
    posts.pop(post_index)
    save_data(posts)


def update_post(updated_post):
    """
     Replaces a blog post with the modified
     blog entry and forwards it for saving.
    :param updated_post: Revised blog post as dictionary
    """
    try:
        updated_post = post_validation(updated_post)
    except (TypeError, KeyError) as error:
        return {'error': error}
    posts = get_posts()
    for index, post in enumerate(posts):
        if post['id'] == updated_post['id']:
            posts[index] = updated_post
            save_data(posts)
