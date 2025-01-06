#!/usr/bin/python3
"""
Script that filters states by user input
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

    # Format the query to include the user input
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        # Print results in the specified format
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    # Clean up
    cursor.close()
    db.close()
