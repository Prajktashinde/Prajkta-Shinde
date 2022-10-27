from unicodedata import name
from flask import Flask,render_template
myflask=Flask(__name__)

@myflask.route('/user/<username>')
def user(username):
     return render_template("first.html",uname=username)     

@myflask.route('/')
def python():
    return "Hi, Welcome to python"

@myflask.route('/flask/')
def flask():
     return "Hi,Welcome to flask"

if __name__=="__main__":
    myflask.run(debug=True)
