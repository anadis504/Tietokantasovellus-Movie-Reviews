from app import app
from flask import render_template, request, redirect
import users, movies

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Username or password incorrect")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/signup", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Registration did not succeed")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search" methods="get")
def search_movie_by_title():
    title = request.args["title"]
    print(title)
    movie_id = movies.movie_id(title)
    if movie_id == 0:
        title = "Movie: " + title + "is not in the database"
        return render_template("movie.html", title=title, reviews=reviews)
    reviews = movies.movie_reviews(title)
    print(len(reviews))
    return render_template("movie.html", title=title, reviews=reviews,movie_id=movie_id)

@app.route("/add_review", methods=["post"])
def add_review():
    movie_id = request.form["movie_id"]
    content = request.form["content"]
    score = request.form["score"]
    if movies.save_review(movie_id, content, score):
        return redirect("/")
    else:
        return render_template("error.html",message="Review did not succeed")

@app.route("/add_movie", methods=["get","post"])
def add_movie():
    if request.method == "GET":
        return render_template("newmovie.html")
    if request.method == "POST":
        title = request.form["tilte"]
        year = request.form["year"]
        genres = request.form.getlist("genre")
        return render_template("newmovie.html")
    
    
    
    
    
    
    
    
    
    
    
