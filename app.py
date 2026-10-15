import sqlite3


def get_user(username):
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Intentionally vulnerable: unsafe SQL string construction for SAST testing
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    print(get_user("test"))
