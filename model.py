import sqlite3


def check_user_existence(username):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('user_credentials.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute the SELECT statement with the WHERE clause to check for the username
    cursor.execute('SELECT COUNT(*) FROM user_credentials WHERE username = ?', (username,))

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Check if the count is greater than 0, indicating the user exists
    if result[0] > 0:
        return True
    else:
        return False


def show_color(username):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('user_credentials.db',check_same_thread=False)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

   

    # Select the username and password from the table
    cursor.execute(f"""SELECT color FROM user_credentials WHERE username = '{username}' ORDER BY id DESC;""")
    # Fetch the result (if any)
    color = cursor.fetchone()[0]


    conn.commit()
    cursor.close()
    conn.close()
    message = f"{username}'s favorite color is {color}"
    return color

# Function to save a new user's credentials
def save_user_credentials(username, password,color="white"):
    conn = sqlite3.connect('user_credentials.db',check_same_thread=False)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table to store usernames and passwords
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            color TEXT NOT NULL
            
        )
    '''
    )

    # Insert the new user's credentials into the table
    cursor.execute('INSERT INTO user_credentials (username, password,color) VALUES (?, ?, ?)', (username, password, color))
    # Commit the changes to the database
    conn.commit()


def show_all():
        # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('user_credentials.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute the SELECT statement to fetch all rows from the table
    cursor.execute('SELECT * FROM user_credentials')

    # Fetch all the results
    results = cursor.fetchall()
    for each in results:
        print(each)
    # Close the cursor and the connection
    cursor.close()
    conn.close()



if __name__ == '__main__':
    #save_user_credentials("usman","ali","yellow")
    #print(show_color("usman"))
    #show_all()
    print(check_user_existence("applesadasd"))