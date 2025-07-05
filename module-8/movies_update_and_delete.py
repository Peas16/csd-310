# Paul Fralix, 07/05/2025, Assignment 8.2 
# This will securely connect to MySQL database and update and delete movies table

""" import statements """
import mysql.connector
from mysql.connector import Error, errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True,
}

def show_films(cursor, title):
    """Function to query the database and display film records with inner joins"""

    # inner join query
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and disply the results
    for film in films:
        print("Film Name: {},\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    """ try/catch block for handling potential MySQL errors """
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # Display current films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film (using an existing studio & genre id)
    cursor.execute("""
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES ('The Day the Earth Stood Still','2008','104', 'Scott Derrickson', 1, 2)
    """)
    db.commit()

    # Display films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the film Alien to be Horror (assuming genre_id=1 is Horror)
    cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien'
    """)
    db.commit()

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the film Gladiator
    cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """)
    db.commit()

    # Display films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


except mysql.connector.Error as err:
    """ on error code """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    """ close the connection to MySQL """
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\n Database connection closed.")
