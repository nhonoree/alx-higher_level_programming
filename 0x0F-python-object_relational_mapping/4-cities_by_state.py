#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Query to join cities and states tables and sort results
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    # Execute query
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        # Print each result row
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    # Clean up
    cursor.close()
    db.close()
