DROP TABLE IF EXISTS 
	users,
	movies,
	genres,
	reviews,
	movie_genres
	CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT NOT NULL);


CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
	title TEXT NOT NULL UNIQUE,
	year SMALLINT NOT NULL CHECK (year > 0));


CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
	genre TEXT NOT NULL UNIQUE);


CREATE TABLE reviews (
	id SERIAL PRIMARY KEY, 
	content TEXT,
	user_id INTEGER REFERENCES users,
	movie_id INTEGER REFERENCES movies,
	score SMALLINT CHECK (score >= 0 AND score <= 5),
	created TIMESTAMP);

	
CREATE TABLE movie_genres (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies,
    genre_id INTEGER REFERENCES genres);
	
	
INSERT INTO genres(genre) VALUES('Action');
INSERT INTO genres(genre) VALUES('Adventure');
INSERT INTO genres(genre) VALUES('Fiction');
INSERT INTO genres(genre) VALUES('Drama');
INSERT INTO genres(genre) VALUES('Comedy');
INSERT INTO genres(genre) VALUES('Horror');
INSERT INTO genres(genre) VALUES('Western');
INSERT INTO genres(genre) VALUES('Crime');
INSERT INTO genres(genre) VALUES('Mystery');
INSERT INTO genres(genre) VALUES('Romance');

INSERT INTO movies(title,year) values('Once upon a time', 1909),('Titanic 2',2200),('Best movie ever', 1430);

INSERT INTO users(username,password) values('bana',123),('bob',123);

INSERT INTO reviews(user_id,movie_id,content,created,score) VALUES (1,1,'very good movie',now(),4)
