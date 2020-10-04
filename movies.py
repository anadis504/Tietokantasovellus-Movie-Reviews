from db import db
from flask import session
import users

def movie_reviews(mov_id):
    
    print(mov_id)
    sql = "SELECT m.title, u.username, r.content, r.created, r.score FROM reviews r LEFT JOIN users u ON u.id = r.user_id LEFT JOIN movies m ON m.id = r.movie_id WHERE m.id = :id ORDER BY r.created DESC LIMIT 25;"
    result = db.session.execute(sql, {"id":mov_id})
    print("We are here!")
    reviews = result.fetchall()
    print(reviews)
    return reviews
        
def get_movie_list(title):
    mov_ids = movie_id(title)
    print(mov_ids)
    if mov_ids != 0:
        
        sql = "SELECT m.id, m.title, m.year FROM movies m WHERE m.id = ANY(:ids);"
        result = db.session.execute(sql, {"ids":mov_ids})
        movie_list = result.fetchall()
        return movie_list
    return 0;
        
def movie_id(title):
    sql = "SELECT id FROM movies WHERE title LIKE :title"
    result = db.session.execute(sql, {"title":"%"+title+"%"})
    idlist = result.fetchall()
    if  len(idlist) != 0:
        print("Id is not none??")
        print(len(idlist))
        print(type(idlist))
        ids = []
        for subl in idlist:
            for item in subl:
                if item != 0 and item != None:
                    ids.append(item)
        print(ids)
        return ids    
    print("Nothing is found")
    return 0

def save_review(movie_id, content, score):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (user_id, movie_id, content, created, score) VALUES (:user_id, :movie_id, :content, NOW(), :score)"
    result = db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id, "content":content, "score":score})
    db.session.commit()
    return True
    
def save_movie(title, year, genres):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO movies (title, year) VALUES (:title, :year) RETURNING id;"
    result = db.session.execute(sql, {"title":title, "year":year})
    mov_id = result.fetchone()[0]
    db.session.commit()
    if mov_id != 0:
        for genre in genres:
            sql = "INSERT INTO movie_genres (movie_id, genre_id) VALUES (:movie_id, :genre_id)"
            db.session.execute(sql, {"movie_id":mov_id, "genre_id":genre})
            print(genre)
        db.session.commit()
        return True
    return False

def movie_with_genres(mov_id):
    sql = "SELECT m.title, m.year, g.genre, COALESCE(g.id,0) FROM movies m LEFT JOIN movie_genres mg ON m.id = mg.movie_id LEFT JOIN genres g ON mg.genre_id = g.id WHERE m.id = :id;"
    result = db.session.execute(sql, {"id":mov_id})
    title_genres = result.fetchall()
    return title_genres

def get_by_score():
    sql = "SELECT m.id, m.title, m.year, COALESCE(CAST(AVG(r.score) AS DECIMAL (10,1)),0) s FROM movies m LEFT JOIN reviews r ON m.id = r.movie_id GROUP BY m.id ORDER BY s DESC LIMIT 20;"
    result = db.session.execute(sql)
    top_movies = result.fetchall()
    return top_movies

def get_movielist_by_genre(genre_id):
    sql = "SELECT m.id, m.title, m.year, g.genre FROM movies m LEFT JOIN movie_genres mg ON m.id=mg.movie_id LEFT JOIN genres g ON g.id=mg.genre_id WHERE g.id=:id;"
    result = db.session.execute(sql, {"id":genre_id})
    movie_list = result.fetchall()
    print(len(movie_list) + " " + type(movie_list) + " " + movie_list)
    return movie_list





