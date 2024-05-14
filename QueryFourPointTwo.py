import mysql.connector

# ** Assingment13 FBI query
def fbi_query(cursor):
    actor_name = input("Enter actor's name: ") # Once deciding on what option you want ...
    query = f"""
        SELECT f.title AS film_title, r.rental_date, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, 
               a.address, a.phone, ci.city, a.postal_code AS zip_code, CONCAT(s.first_name, ' ', s.last_name) AS clerk_name,
               (SELECT phone FROM address WHERE address_id = s.address_id) AS store_phone
        FROM rental r
        JOIN inventory i ON i.inventory_id = r.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN customer c ON r.customer_id = c.customer_id
        JOIN address a ON c.address_id = a.address_id
        JOIN city ci ON a.city_id = ci.city_id
        JOIN staff s ON r.staff_id = s.staff_id
        JOIN film_actor fa ON f.film_id = fa.film_id
        JOIN actor ac ON fa.actor_id = ac.actor_id
        JOIN store st ON s.store_id = st.store_id
        WHERE CONCAT(ac.first_name, ' ', ac.last_name) = '{actor_name}';
    """
    cursor.execute(query) # This will execute the query based off of the info provided
    result = cursor.fetchall()
    if result:
        print("Rentals featuring", actor_name + ":")
        for row in result:
            print("Film:", row[0])
            print("Rental Date:", row[1])
            print("Customer Name:", row[2])
            print("Address:", row[3])
            print("Phone:", row[4])
            print("City:", row[5])
            print("Zip Code:", row[6])
            print("Clerk Name:", row[7])
            print("Store Phone:", row[8])
            print()
    else:
        print("No rentals found for", actor_name)

# calling query 1
def query_1(cursor):
    actor_name = input("Enter actor's name (e.g., 'Tom Hanks'): ")
    query = f"""
        SELECT film.title, actor.first_name, actor.last_name
        FROM film
        INNER JOIN film_actor ON film.film_id = film_actor.film_id
        INNER JOIN actor ON film_actor.actor_id = actor.actor_id
        WHERE CONCAT(actor.first_name, ' ', actor.last_name) = '{actor_name}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print(f"Films featuring {actor_name}:")
        for row in result:
            print("Film:", row[0])
            print("Actor:", row[1], row[2])
            print()
    else:
        print("No films found for", actor_name)

# calling query 2
def query_2(cursor):
    category_name = input("Enter category name (e.g., 'Action'): ")
    query = f"""
        SELECT film.title, GROUP_CONCAT(CONCAT(actor.first_name, ' ', actor.last_name) SEPARATOR ', ') AS actors
        FROM film
        INNER JOIN film_actor ON film.film_id = film_actor.film_id
        INNER JOIN actor ON film_actor.actor_id = actor.actor_id
        INNER JOIN film_category ON film.film_id = film_category.film_id
        INNER JOIN category ON film_category.category_id = category.category_id
        WHERE category.name = '{category_name}'
        GROUP BY film.title;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print(f"Films in category '{category_name}':")
        for row in result:
            print("Film:", row[0])
            print("Actors:", row[1])
            print()
    else:
        print("No films found in category", category_name)

# calling query 3
def query_3(cursor):
    rental_date = input("Enter rental date (YYYY-MM-DD): ")
    query = f"""
        SELECT film.title, CONCAT(customer.first_name, ' ', customer.last_name) AS customer_name,
               address.address, address.phone
        FROM rental
        JOIN inventory ON rental.inventory_id = inventory.inventory_id
        JOIN film ON inventory.film_id = film.film_id
        JOIN customer ON rental.customer_id = customer.customer_id
        JOIN address ON customer.address_id = address.address_id
        WHERE rental.rental_date = '{rental_date}';
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        print(f"Customers who rented films on {rental_date}:")
        for row in result:
            print("Film:", row[0])
            print("Customer Name:", row[1])
            print("Address:", row[2])
            print("Phone:", row[3])
            print()
    else:
        print("No rentals found for", rental_date)


# main function for sql connector
def main():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hector3463",
            database="sakila"
        )
        cursor = conn.cursor()

        # Menu options
        menu = """
        Menu:
        1. FBI Query
        2. Query 1: Find all films with a given actor's name
        3. Query 2: Find all films of a given category and list them with their actors
        4. Query 3: Find the customers that rented films on a given date
        q. Quit
        """
        while True:
            print(menu)
            choice = input("Enter your choice: ")

            if choice == '1':
                fbi_query(cursor)
            elif choice == '2':
                query_1(cursor)
            elif choice == '3':
                query_2(cursor)
            elif choice == '4':
                query_3(cursor)
            elif choice == '5':
                m14_queries(cursor)
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice. Please try again.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
