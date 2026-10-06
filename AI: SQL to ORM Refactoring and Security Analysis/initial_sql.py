import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="example_db"
    )


def create_user(db_cursor, username, email):
    """Create a new user safely using parameterized queries."""
    if not username or not email:
        print("Username and email are required.")
        return
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    try:
        db_cursor.execute(sql, (username, email))
        print(f"User '{username}' created successfully.")
    except Error as e:
        print(f"Error creating user: {e}")


def get_user_by_username(db_cursor, username):
    """Fetch a single user by username."""
    sql = "SELECT id, username, email FROM users WHERE username = %s"
    try:
        db_cursor.execute(sql, (username,))
        return db_cursor.fetchone()
    except Error as e:
        print(f"Error fetching user: {e}")
        return None


def update_user_email(db_cursor, username, new_email):
    """Update a user's email address."""
    sql = "UPDATE users SET email = %s WHERE username = %s"
    try:
        db_cursor.execute(sql, (new_email, username))
        if db_cursor.rowcount == 0:
            print(f"No user found with username '{username}'.")
        else:
            print(f"Email for '{username}' updated successfully.")
    except Error as e:
        print(f"Error updating user: {e}")


def delete_user(db_cursor, username):
    """Delete a user by username."""
    sql = "DELETE FROM users WHERE username = %s"
    try:
        db_cursor.execute(sql, (username,))
        if db_cursor.rowcount == 0:
            print(f"No user found with username '{username}'.")
        else:
            print(f"User '{username}' deleted successfully.")
    except Error as e:
        print(f"Error deleting user: {e}")


def list_users(db_cursor):
    """Return all users."""
    sql = "SELECT id, username, email FROM users"
    try:
        db_cursor.execute(sql)
        return db_cursor.fetchall()
    except Error as e:
        print(f"Error listing users: {e}")
        return []


if __name__ == "__main__":
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "username VARCHAR(50) UNIQUE NOT NULL, "
            "email VARCHAR(100) UNIQUE NOT NULL)"
        )
        create_user(cursor, "carlos", "carlos@example.com")
        conn.commit()
        print(get_user_by_username(cursor, "carlos"))
        print(list_users(cursor))
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
