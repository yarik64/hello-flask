#!/usr/bin/env python3


from flask import Flask
from flask import url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
def root():
    return url_for('static', filename='index.html')


@app.route("/index.html")
def index():
  return render_template('index.html',
                         styles=url_for('static', filename='styles.css')
                         )


@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/about')
def about():
  return 'This is the about page'


@app.route('/user/<username>')
def show_user_profile(username):
  return f'User {username}'


if __name__ == '__main__':
  app.run(debug=True)
