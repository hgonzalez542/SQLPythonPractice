import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="Hector3463",
    database="sakila"
)

myCursor = mydb.cursor()

myCursor.execute('SELECT film.title, actor.first_name, actor.last_name FROM film '
                  + ' JOIN film_actor ON film.film_id = film_actor.film_id'
                  + ' JOIN actor ON film_actor.actor_id = actor.actor_id INNER JOIN film_category ON film.film_id = film_category.film_id ' 
                  + ' JOIN category ON film_category.category_id = category.category_id WHERE category.name = "Action";')
myResult = myCursor.fetchall()
for x in myResult:
    print(x)