from flask import Flask, request, render_template
import urllib
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        global value
        value = request.form['comment']
        print(value)
    return render_template("contact.html")

@app.route('/memo')
def memo():
    return render_template("memo.html", memo=value)

if __name__ == '__main__':
    app.run(debug=True)
