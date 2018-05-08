from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from config import get_config
from data import article_model
import flask_login
import initialization
from data import DBClient

app = Flask(__name__)
app.secret_key = get_config()['APP_SECRET']

# This should be deprecated soon.
username=None

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    # This method requires every path to check if the user is logged in.
    # A better solution would be to customise the anonymous user class, as seen:
    # https://teamtreehouse.com/community/attributeerror-anonymoususermixin-object-has-no-attribute-username
    if flask_login.current_user.is_authenticated:
        username = flask_login.current_user.id
    else: username = None

    posts = article_model.get_breaking()

    return render_template('posts.html', posts=posts, username=username)


@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html', username=username)


@app.route('/keyword')
@app.route('/keyword.html')
def keyword():
    return render_template('keyword.html', username=username)

@app.route('/keyword/<query>')
def keywordsearch(query):
    return render_template('keywordsearch.html', query=query)


@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html', username=username)


@app.route('/settings')
@app.route('/settings.html')
def settings():
    return render_template('settings.html', username=username)


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', username=username)
    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    # This is just an example page to show pages protected by login.
    return 'Logged in as: ' + flask_login.current_user.id


class User(flask_login.UserMixin):
    pass


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/signup', methods=['GET', 'POST'])
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        return "Cool my dude"
    else:
        return render_template('signup.html', username=username)


if __name__ == '__main__':
    client = DBClient()
    initialization.init_database()
    app.run()