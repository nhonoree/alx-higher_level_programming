#!/usr/bin/python3
import sys
import MySQLdb

def main():
    # Check if the script is executed with the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_user> <mysql_password> <database_name> <state_name>")
        return
    
    # Assign the arguments to variables
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    try:
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to filter states by name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        
        # Fetch all rows and print them
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
