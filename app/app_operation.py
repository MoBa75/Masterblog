from app.json_storage import get_data


def create_new_id():
    posts = get_data()
    new_id = posts[-1]['id'] + 1
    print(new_id)
    return new_id
