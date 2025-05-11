from app.json_storage import get_data


def create_new_id():
    """

    :return:
    """
    posts = get_data()
    # default value for the first comment
    new_id = 1
    id_lst = [int(post["id"]) for post in posts if "id" in post
              and str(post.get("id", "")).isdigit()]
    new_id = next(num for num in range(1, len(posts)+2) if num not in id_lst)
    return new_id
