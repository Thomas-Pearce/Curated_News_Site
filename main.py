from flask import Flask, render_template
# from this import create_app
# app = create_app('config.yml')
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return 'Hello World!'



if __name__ == '__main__':
    app.run()