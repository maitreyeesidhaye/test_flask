import sqlite3

# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

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
    c1.execute("INSERT INTO users_test (name, age) VALUES(?, ?)",
               (name, age))
    connie.commit()
    connie.close()


def get_user_login_data(name):
    """ Returns user login based on email in the dictionary format """

    conn1 = sqlite3.connect(URI)
    c2 = conn1.cursor()
    col_cursor = c2.execute('select * from users_test')
    user_table_col_names = list(map(lambda x: x[0], col_cursor.description))
    c2.execute("SELECT * FROM users_test WHERE name = ?", (name,))
    data = c2.fetchall()
    conn1.close()
    user_dic = {}
    for i in range(len(data[0])):
        user_dic[user_table_col_names[i]] = data[0][i]
    return user_dic


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, Girl!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        print(name, age)
        insert_user(name, age)
        xx = get_user_login_data(name)
        print(xx)
    return render_template('login.html')


if __name__ == "__main__":  # on running python app.py
    app.run(port=5001)  # run the flask app
