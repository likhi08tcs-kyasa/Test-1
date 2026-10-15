import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_user(username):
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


@app.route("/user")
def user():
    return str(get_user(request.args.get("username", "")))


if __name__ == "__main__":
    app.run()
