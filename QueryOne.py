import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="Hector3463",
    database="sakila"
)

myCursor = mydb.cursor()

myCursor.execute('SELECT film.title FROM film JOIN film_actor ON film.film_id = film_actor.film_id'
                 + ' JOIN actor ON film_actor.actor_id = actor.actor_id WHERE actor.first_name = "Penelope" AND actor.last_name="Guiness"')
myResult = myCursor.fetchall()
for x in myResult:
    print(x)