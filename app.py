from flask import Flask, render_template, request, redirect, url_for, abort
from app.json_storage import get_posts, save_post, delete_post, update_post
from app.app_operation import create_new_id

app = Flask(__name__)


@app.route('/')
def index():
    """
    Calls the index HTML page and lists the saved
    blog entries with a preview of the entries
    """
    posts = get_posts()
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
            abort(404, description="Author, title and content needed!")
        posts = get_posts()
        new_post = {"id": create_new_id(posts),
                    "author": author,
                    "title": title,
                    "content": content
                    }
        save_post(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route("/posts/<int:post_id>")
def post_details(post_id):
    """
    Calls up the HTML page for the selected
    blog entry and displays the entire entry.
    """
    posts = get_posts()
    for post in posts:
        if post["id"] == post_id:
            return render_template("post.html", post=post)
    abort(404, description=f'Post with ID {post_id} not found.')


@app.route('/delete/<int:post_id>', methods=['GET', 'DELETE', 'POST'])
def delete(post_id):
    """
    Calls up an HTML page with the selected blog post for deletion.
    Allows blog post deletion and then returns to the main page (index).
    """
    posts = get_posts()
    if request.method in ['POST', 'DELETE']:
        for post_index, post in enumerate(posts):
            if post["id"] == post_id:
                delete_post(post_index)
                return redirect(url_for('index'))
        abort(404, description=f'Post with ID {post_id} not found.')
    for post in posts:
        if post["id"] == post_id:
            return render_template("delete.html", post=post)
    abort(404, description=f'Post with ID {post_id} not found.')


@app.route('/update/<int:post_id>', methods=['GET', 'PUT', 'POST'])
def update(post_id):
    """
    Calls up the update HTML page with the contents of the selected blog entry and
    gives the user the option of updating the entries. Replaces the blog entry with
    the user input and forwards it for saving.
    """
    posts = get_posts()
    if request.method in ['POST', 'PUP']:
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        if not author or not title or not content:
            abort(404, description="Author, title and content needed!")
        updated_post = {"id": post_id,
                        "author": author,
                        "title": title,
                        "content": content
                        }
        update_post(updated_post)
        return redirect(url_for('index'))
    for post in posts:
        if post["id"] == post_id:
            return render_template("update.html", post=post)
    abort(404, description=f'Post with ID {post_id} not found.')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
