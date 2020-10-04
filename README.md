# Tietokantasovellus-Movie-Reviews

Movie reviews will be a database application where users can add movie-reviews. Users will be able to 
* add movies to the database, 
* search for already existing movies and 
* read other users reviews. 
* Other users may like and upvote (or maybe also downvote) some reviews so that the most liked/popular/suited reviews stay on top. In other words, the list of the reviews is ordered by users votes. 
* The amount of the reviews could also be limited. 
* Maybe also add a feature where the movies may be sorted by: 
1. genre
2. popularity (score) 
3. other critereas.

So one can search for a given genre and get a list sorted by the highest scores.

* The same movie cannot be added to the database twice, that is if "Titanic" is in the database and one wants to review it one has to add a review to the already existing movie "Titanic" and not add a new "Titanic" to review.

The application will be written in Python. The users will have to authenticate themselves to the application (sing in) so that the users may be identified by their usernames. The application will have to have a possibility for signing up (creating a usersname+password).

## As of 20.09.2020
The application has some codes and features. 
* The registering of users is working
* Signing in, logging out
* It is possible to search for a movie already in db and read the reviews, (signed in users can add reviews)
* Adding movies to database is also now working

Next steps:
* make the code more error resistent
* definitely do something about the layout
* add features as mentioned above

The result.fetchone() does not work and gives a lot of errors all the time. For example this line of code form Osa 2, Esimerkki: Kyselyt:
    
    sql = "INSERT INTO polls (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    poll_id = result.fetchone()[0]
    
does not work with me as it is explained to do in the materials. Now the adding of reviews does not work in heroku so I have to fix this later somehow. Would love to get some advice!!! Or otherwise if my code is somehow totally weird (this is my first time with python) would love to hear about it.

I have removed the fetchone()[0] things and now it somehow works.

The app can be tested at https://fast-atoll-48246.herokuapp.com/

## As of 4.10.2020
The application has most of its features
* Not registered visitors may search for movies and read other's reviews
* Registered logged in users can add movies to database and post reviews
* Forms are validated and errormessages are displayed
* Movies can be displayed by genre by clicking the genre link in a movie-site. I should probably add the feature to the startpage also though.
* Bootstrap4 is implemented for layout and form validation. Form validation is also implemented at the database levels.
##### Other features I would like to implement:
* CSS for more customized layout
* Down- and up-voting of reviews so that the most popular (upvoted) reviews are listed first. Also restrict the number of reviews shown (Not yet implemented)
* Maybe add a function for showing some sort of a profile page listing a users reviews if I have the time.

The app can be tested at https://fast-atoll-48246.herokuapp.com/
