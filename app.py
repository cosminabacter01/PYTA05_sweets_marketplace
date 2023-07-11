"""
Entrypoint-ul in aplicatia noastra web
dezvoltata folosind framework-ul Flask.

pip install flask
"""

from flask import Flask, render_template, request, redirect

from db.db_connection import create_database
from models.user import User

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # urmeaza logica asociata cu metoda POST
    user_data = dict(request.form) # => dictionar cu informatiile venite din form
    # user_obj = User(email=user_data["email"], password=user_data["password"])
    try:
        user_obj = User(**user_data)
        user_obj.check_in_db()
    except Exception as e:
        return render_template("login.html", error=f"{e}")
    print("=============================")
    print(user_data)
    return redirect('/products')


@app.route('/products', methods=["GET"])
def get_all_products():
    return render_template("products_list.html")


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=7000)
