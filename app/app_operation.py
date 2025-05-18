def create_new_id(posts):
    """
    Creates a new unique ID for a blog entry,
    fills in missing ID numbers.
    :return: A unique ID numer as integer.
    """
    id_lst = [int(post["id"]) for post in posts if "id" in post
              and str(post.get("id", "")).isdigit()]
    new_id = next(num for num in range(1, len(posts) + 2) if num not in id_lst)
    return new_id


def post_validation(post):
    """
    Checks if a post is valid.
    :param post: The post to check as dictionary
    :return: The post as dictionary
    :raises: TypeError, KeyError if invalid
    """
    if not post or not isinstance(post, dict):
        raise TypeError("Error: Update element needs to be dictionary!")
    if not len(post) == 4:
        raise KeyError("Error: 'id', 'author', 'title', 'content' need to exist!")
    for key in post:
        if key not in ['id', 'author', 'title', 'content']:
            raise KeyError(f"Error: Wrong key '{key}'!")
    return post
