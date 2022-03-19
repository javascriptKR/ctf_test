from flask import Flask, request, render_template
import bot
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
    global content
    if request.method == 'POST':
        content = request.form['comment']
        bot.check(content)
        return render_template("contact.html", value="admin에게 메일을 보냈습니다.")

    return render_template("contact.html")

@app.route('/profile', methods=['GET','POST'])
def profile():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if request.method == 'POST':
        if request.form['userip'] == ip and request.form['status'] == 'on':
            print(request.form)

        return render_template("profile.html", ip=ip, msg="You're not admin.")

    return render_template("profile.html", ip=ip)

@app.route('/private')
def memo():
    txt = "Your account has not been validated by an admin."
    return render_template("private.html", text=txt)

if __name__ == '__main__':
    app.run(debug=True)
