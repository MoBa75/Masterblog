from flask import Flask, render_template, request, redirect, url_for
from app.json_storage import get_data, create_data, delete_data, update_data
from app.app_operation import create_new_id


app = Flask(__name__)


@app.route('/')
def index():
    """
    Calls the index HTML page and lists the saved
    blog entries with a preview of the entries
    """
    posts = get_data()
    return render_template("index.html", posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Calls up the HTML for new blog entries, creates a new blog
    entry from the user imput and forwards them for storage.
    """
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        if not author or not title or not content:
            return "Author, title and content needed!"
        new_post = {"id": create_new_id(),
                    "author": author,
                    "title": title,
                    "content": content
                    }
        create_data(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route("/posts/<int:post_id>")
def post_details(post_id):
    """
    Calls up the HTML page for the selected
    blog entry and displays the entire entry.
    """
    posts = get_data()
    for post in posts:
        if post["id"] == post_id:
            return render_template("post.html", post=post)
    return "Post not found", 404


@app.route('/delete/<int:post_id>', methods=['GET', 'DELETE', 'POST'])
def delete(post_id):
    """
    Calls up an HTML page with the selected blog post for deletion.
    Allows blog post deletion and then returns to the main page (index).
    """
    posts = get_data()
    if request.method in ['POST', 'DELETE']:
        for post_index, post in enumerate(posts):
            if post["id"] == post_id:
                delete_data(post_index)
                return redirect(url_for('index'))
        return "Post not found", 404
    for post in posts:
        if post["id"] == post_id:
            return render_template("delete.html", post=post)
    return "Post not found", 404


@app.route('/update/<int:post_id>', methods=['GET', 'PUT', 'POST'])
def update(post_id):
    """
    Calls up the update HTML page with the contents of the selected blog entry and
    gives the user the option of updating the entries. Replaces the blog entry with
    the user input and forwards it for saving.
    """
    posts = get_data()
    if request.method in ['POST', 'PUP']:
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        if not author or not title or not content:
            return "Author, title and content needed!"
        updated_post = {"id": post_id,
                        "author": author,
                        "title": title,
                        "content": content
                        }
        update_data(updated_post)
        return redirect(url_for('index'))
    for post in posts:
        if post["id"] == post_id:
            return render_template("update.html", post=post)
    return "Post not found", 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5010, debug=True)
