from db.crud.products_crud import ProductsDb
from db.db_connection import create_database

from flask import Flask, render_template, request, redirect, session

from models.user import User

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", user=session.get("user", False))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user_data = dict(request.form)
    # {"email": "cosmina@yahoo.ro", "password": "123"}
    try:
        # User(email="cosmina@yahoo.ro", password="123")
        user_obj = User(**user_data)
        user_obj.check_in_db()
        session["user"] = user_obj.email
    except Exception as e:
        return render_template("login.html", error=f"{e}")
    return redirect("/products")


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect('/')


@app.route("/users", methods=["GET"])
def get_all_users():
    pass


@app.route("/users/<user_id>", methods=["GET"])
def get_user_by_id():
    pass


@app.route("/users/add", methods=["GET", "POST"])
def add_user():
    if request.method == 'GET':
        return render_template('sign_up.html')
    user_data = dict(request.form)
    try:
        user_obj = User(**user_data)
        user_obj.add()
    except Exception as e:
        return render_template("sign_up.html", error=f"{e}")
    return redirect("/")


@app.route("/users/update/<user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    pass


@app.route("/users/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    pass


@app.route("/products", methods=["GET"])
def get_all_products():
    products_obj = ProductsDb()
    products = products_obj.read()
    return render_template("products_list.html", products=products, user=session.get("user", False))


@app.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    products_obj = ProductsDb()
    products = products_obj.read(id=product_id)
    return render_template("product_details.html", product=products[0], user=session.get("user", False))


if __name__ == '__main__':
    create_database()
    products_crud = ProductsDb()
    products_crud.setup_products('./db/products_setup.json')
    app.run(debug=True, port=7001)
