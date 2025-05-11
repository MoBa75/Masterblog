from app.json_storage import get_data


def create_new_id():
    """
    Creates a new unique ID for a blog entry,
    fills in missing ID numbers.
    :return: A unique ID numer as integer.
    """
    posts = get_data()
    id_lst = [int(post["id"]) for post in posts if "id" in post
              and str(post.get("id", "")).isdigit()]
    new_id = next(num for num in range(1, len(posts)+2) if num not in id_lst)
    return new_id
