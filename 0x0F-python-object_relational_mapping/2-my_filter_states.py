#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database using the identified socket path
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, unix_socket="/var/run/mysqld/mysqld.sock")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Define the query, using the user-provided state name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query
    cursor.execute(query, (state_name,))

    # Fetch the results and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
