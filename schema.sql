DROP TABLE IF EXISTS 
	users,
	movies,
	genres,
	reviews,
	movie_genres
	CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL);


CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
	title TEXT NOT NULL UNIQUE,
	year SMALLINT NOT NULL CHECK (year > 0 AND year < 2050));


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

INSERT INTO movies(title,year) values('Once upon a time', 1909),('Titanic 2',2018),('Best movie ever', 1430),('A dog and a dog, story of two animals',2020),('Another real movie',2003);

INSERT INTO users(username,password) values('uolevi',123),('maija97',123),('Aapeli',123),('Porkkana',123),('bana',123),('bob',123);

INSERT INTO movie_genres(movie_id,genre_id) VALUES(1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(3,7),(3,8),(2,9),(1,10),(4,2),(4,7),(4,8),(4,9),(5,1),(5,3),(5,10);

INSERT INTO reviews(user_id,movie_id,content,created,score) VALUES (1,1,'Very good movie',now(),4),(2,1,'Recomend to see',now(),2),(3,2,'Amazing movie, incredible plot, beautiful scenary. Totally my new favorite',now(),5),(4,4,'Luckily no animals or vegetables were harmed during the filming',now(),3);
