#!/usr/bin/python3
"""
Script that filters states by user input safely, preventing SQL injection
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

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    try:
        cursor.execute(query, (sys.argv[4],))
        results = cursor.fetchall()

        # Print results in the specified format
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")

    # Clean up
    cursor.close()
    db.close()
