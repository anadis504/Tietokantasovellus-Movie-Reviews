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
            return render_template("error.html", message="Username or password incorrect")

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
        if username == "":
            print("Empty username detected")
            return render_template("error.html", message="Registration did not succeed")
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration did not succeed")

@app.route("/")
def index():
    top_movies = movies.get_by_score()
    return render_template("index.html", movies=top_movies)

@app.route("/search", methods=["get"])
def search_movie_by_title():
    title = request.args["title"]
    print(title)
    movie_list = movies.get_movie_list(title)
    if movie_list == 0:
        title = "Movie: " + title + "is not in the database"
        return render_template("error.html", message=title)
    return render_template("movielist.html", title="Search result for: "+title, movies= movie_list)

@app.route("/search/<int:genre_id>")
def search_movie_by_genre(genre_id):
    print(genre_id)
    if genre_id == 0:
        title = "No genre selected"
        return render_template("error.html", message=title)
    movie_list = movies.get_movielist_by_genre(genre_id)
    title = "Search result for genre: " + movie_list[0][3]
    return render_template("movielist.html", title=title, movies= movie_list)

@app.route("/show_reviews/<int:m_id>")
def show_reviews(m_id):
    movie_genres = movies.movie_with_genres(m_id)
    reviews = movies.movie_reviews(m_id) 
    return render_template("movie.html", reviews=reviews, movie_id=m_id, specs=movie_genres) 

@app.route("/add_review", methods=["post"])
def add_review():
    movie_id = request.form["movie_id"]
    content = request.form["content"]
    score = request.form["score"]
    if movies.save_review(movie_id, content, score):
        return redirect("/show_reviews/"+movie_id)
    else:
        return render_template("error.html",message="Review did not succeed")

@app.route("/add_movie", methods=["get","post"])
def add_movie():
    if request.method == "GET":
        return render_template("newmovie.html")
    if request.method == "POST":
        print("know the mothod at least")
        title = request.form["title"]
        year = request.form["year"]
        genres = request.form.getlist("genre")
        print("got so far")
        if movies.save_movie(title, year, genres):
            return redirect ("/")
        else:
            return render_template("error.html",message="Movie not added")
    
    
    
    
    
    
    
    
    
    
