from flask import Flask, render_template
app = Flask(__name__)
username=None
# username="Tom"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():

    filler="""This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.
    This is a bunch more text just to fill it outThis is a bunch more text just to fill it outThis is a bunch more text just to fill it outThis is a bunch more text just to fill it outThis is a bunch more text just to fill it out
    This is a bunch more text just to fill it outThis is a bunch more text just to fill it outThis is a bunch more text just to fill it outThis is a bunch more text just to fill it out
    This is a bunch more text just to fill it out
    """
    posts = [
        {
            'image': './static/images/cat.jpg',
            'title': 'Post One',
            'body': filler,
            'updated': 'Last updated 3 mins ago'
        },
        {
            'image': './static/images/cat.jpg',
            'title': 'Post Two',
            'body': filler,
            'updated': 'Last updated 3 mins ago'
        }
    ]
    return render_template('posts.html', posts=posts, username=username)


@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html', username=username)


@app.route('/keyword')
@app.route('/keyword.html')
def keyword():
    return render_template('keyword.html', username=username)


@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html', username=username)


@app.route('/settings')
@app.route('/settings.html')
def settings():
    return render_template('settings.html', username=username)


@app.route('/login')
@app.route('/login.html')
def login():
    return render_template('login.html', username=username)

@app.route('/signup')
@app.route('/signup.html')
def signup():
    return render_template('signup.html', username=username)


if __name__ == '__main__':
    app.run()