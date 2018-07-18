# coding=utf-8
import time

from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",
                           title='Home',  # title没有也诶啥关系，这个字段在html里会被忽略
                           user=user)


@app.route('/index1')
def index1():
    '''comment'''
    user = {'nickname': 'Miguel'}  # fake user
    return '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
      </body>
    </html>
    '''


@app.route('/index2')
def index2():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index2.html",
                           title='Home',  # title没有也诶啥关系，这个字段在html里会被忽略
                           user=user)

@app.route('/test')
def test():
    user = {'nickname': 'Miguel'}  # fake user
    return dict(),204


@app.route('/index3')
def index3():
    user = {'nickname': 'Miguel'}  # fake user
    if int(time.time()) % 2 == 0:
        return render_template("index3.html",
                               user=user)
    else:
        return render_template("index3.html",
                               title='Home',
                               user=user)
