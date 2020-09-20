from db import db
from flask import session

def movie_reviews(title):
    id = movie_id(title)
    if id != 0:
        sql = "SELECT * FROM movie_reviews mr WHERE mr.movie_id=:id"
        result = db.session.execute(sql, {"id":id})
        print(result)
        print("what is this")
        return ("/")
    else:
        print("No movie found")
        return("No movie for you")
        

def movie_id(title):
    sql = "SELECT id FROM movies WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    if result.fetchone() != None:
        return result.fetchone()    
    print("The result is that is found that is is this that is Nothing is found")
    return 0

