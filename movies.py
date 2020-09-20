from db import db
from flask import session
import users

def movie_reviews(title):
    id = movie_id(title)
    print(id)
    if id != 0:
        sql = "SELECT m.title, u.username, r.content, r.created, r.score FROM reviews r LEFT JOIN users u ON u.id=r.user_id LEFT JOIN movies m ON m.id = r.movie_id WHERE m.id=:id ORDER BY r.created DESC;"

        result = db.session.execute(sql, {"id":id})
        reviews = result.fetchall()
        print(reviews)
        return(reviews)
    else:
        print("No movie found")
        return("No movie found")
        

def movie_id(title):
    sql = "SELECT id FROM movies WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    id = result.fetchone()[0]
    if  id != None:
        print("or here??")
        print(id)
        return id    
    print("Nothing is found")
    return 0

def save_review(movie_id, content, score):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (user_id, movie_id, content, created, score) VALUES (:user_id, :movie_id, :content, NOW(), :score)"
    result = db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id, "content":content, "score":score})
    if result.fetchone()[0] != 0:
        db.session.commit()
        return True
    return False

def save_movie(title, year, genres):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO movies (title, year) VALUES (:title, :year)"
    result = db.session.execute(sql, {"title":title, "year":year})
    db.session.commit()
    id = movie_id(title)
    if id != 0:
        for genre in genres:
            sql = "INSERT INTO movie_genres (movie_id, genre_id) VALUES (:movie_id, :genre_id)"
            db.session.execute(sql, {"movie_id":id, "genre_id":genre})
        db.session.commit()
        return True
    return False



