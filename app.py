import sqlite3
from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance

URI = "/Users/maitreyeesidhaye/Desktop/test_flask/test_db.db"
CREATE_USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users_test (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        age text NOT NULL
                                        ); """

conn = sqlite3.connect(URI)
c = conn.cursor()
c.execute(CREATE_USERS_TABLE)
conn.close()


def insert_user(name, age):
    """ Add basic user login details to users table """
    # Inserts new record in db.collection (data must be in JSON)
    connie = sqlite3.connect(URI)
    c1 = connie.cursor()
    c1.execute("INSERT INTO users (name, age) VALUES(?, ?)",
              (name, age))
    connie.commit()
    connie.close()


@app.route("/")  # at the end point /
def hello():  # call method hello
    return "Hello World!"  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run(port=5001)  # run the flask app
