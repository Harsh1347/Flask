from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = "xhuYal08Bjs"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['name']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:    
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user",methods = ['POST','GET'])
def user():
    if "user" in session:
        user = session['user']
        return f"your username is {user}"
    else :
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)