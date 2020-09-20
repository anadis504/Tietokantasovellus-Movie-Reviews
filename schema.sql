DROP TABLE IF EXISTS users, movies, genres, reviews, movie_reviews CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR (24) UNIQUE,
	password VARCHAR(32) NOT NULL);


CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
	title VARCHAR (50) NOT NULL UNIQUE,
	year SMALLINT NOT NULL CHECK (year > 0);


CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
	genre VARCHAR (30) NOT NULL UNIQUE);


CREATE TABLE reviews (
	id SERIAL PRIMARY KEY, 
	content TEXT,
	user_id INTEGER REFERENCES users,
	score SMALLINT CHECK (score >= 0 AND score <= 10),
	created TIMESTAMP);


CREATE TABLE movie_reviews (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	review_id INTEGER REFERENCES reviews);
