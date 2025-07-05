# Paul Fralix, 07/04/2025, Assignment 7.2

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

try:
    """ try/catch block for handling potential MySQL errors """
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    # 1. Select all fields from the studio table
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    # 2. Select all fields from the genre table
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # 3. Select movie names for movies less than 2 hours 
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    for film in short_films:
        print("Film Name: {}\nRuntime: {} minutes\n".format(film[0], film[1]))

    # 4. Get list of film names and directors grouped by director
    print("\n-- DISPLAYING Director RECORDS in Grouped Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films_by_director = cursor.fetchall()
    for film in films_by_director:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

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
        print("\n MySQL connection is closed.")
