from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/signup",methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    sqlname = "SELECT COUNT(*) FROM users WHERE username=:username"
    result = db.session.execute(sqlname, {"username":username})
    count = result.fetchone()[0]
    if count != 0:
        return redirect("/")    # TODO: add an error message for the user
    else:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        return redirect("/")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return redirect("/")    # TODO add an error message
    else:
        hash_value = user[0]
        if check_password_hash(hash_value,password):
            session["username"] = username
        else:
            return redirect("/signup")
        return redirect("/signup")


