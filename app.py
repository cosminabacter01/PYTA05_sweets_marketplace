"""
Entrypoint-ul in aplicatia noastra web
dezvoltata folosind framework-ul Flask.

pip install flask
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=7000)
