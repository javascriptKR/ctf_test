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

@app.route('/email')
def email():
    return render_template("email.html")

memo_text = ""

@app.route('/memo')
def memo():
    global memo_text
    text = request.args.get("memo", None)
    if text:
        memo_text += text
    return render_template("memo.html", memo=memo_text)

if __name__ == '__main__':
    app.run(debug=True)