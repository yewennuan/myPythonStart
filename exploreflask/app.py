from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    print url_for('index')
    return 'Hello World!'


@app.route('/index')
def index():
    return 'index!'


if __name__ == '__main__':
    app.run()
