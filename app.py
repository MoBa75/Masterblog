from flask import Flask, render_template, request, redirect, url_for
from app.json_storage import get_data, save_data
from app.app_operation import create_new_id


app = Flask(__name__)


@app.route('/')
def index():
    posts = get_data()
    return render_template("index.html", posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
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
        save_data(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

