import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="Hector3463",
    database="sakila"
)

myCursor = mydb.cursor()

myCursor.execute('SELECT film.title, customer.first_name, customer.last_name, address.address, address.phone FROM film'
                 + ' JOIN inventory ON film.film_id = inventory.inventory_id'
                 + ' JOIN rental ON inventory.inventory_id = rental.inventory_id'
                 + ' JOIN customer ON rental.customer_id = customer.customer_id'
                 + ' JOIN address ON customer.address_id = address.address_id'
                 + ' WHERE rental.rental_date = "2005-05-24 22:53:30"')
myResult = myCursor.fetchall()
for x in myResult:
    print(x)