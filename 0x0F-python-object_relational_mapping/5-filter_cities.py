#!/usr/bin/python3
import MySQLdb
import sys


def list_cities_by_state():
    """Lists all cities of a state from the database"""
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Prepare and execute the query to fetch cities and their state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    cursor.execute(query, (sys.argv[4],))

    # Fetch and print the result
    cities = cursor.fetchall()
    city_list = ', '.join([city[0] for city in cities])
    print(city_list)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
