"""
Setup functions for creating database and tables
"""
import sqlite3

DB_FILE_PATH = "PYTA05_sweets.db"


def get_db_connection(db_path=DB_FILE_PATH):
    connection = sqlite3.connect(db_path)
    return connection


def create_database(db_path=DB_FILE_PATH):
    connection = sqlite3.connect(db_path)
    create_tables(connection)


def create_tables(connection):
    create_users_table(connection)
    create_products_table(connection)
    create_orders_table(connection)
    create_order_line_table(connection)


def create_users_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS Users (
    id TEXT NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
    );
    """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()


def create_products_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS Products (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        price REAL NOT NULL,
        weight_grams INTEGER NOT NULL,
        available_quantity INTEGER NOT NULL DEFAULT 0,
        image TEXT
        );
        """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()


def create_orders_table(connection):
    query = """
            CREATE TABLE IF NOT EXISTS Orders (
            id TEXT NOT NULL PRIMARY KEY,
            user_id FOREIGN_KEY REFERENCES Users(id)
            );
            """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()


def create_order_line_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS Orderlines (
        id TEXT NOT NULL PRIMARY KEY,
        order_id FOREIGN_KEY REFERENCES Orders(id),
        quantity INTEGER NOT NULL,
        subtotal REAL NOT NULL,
        product_id FOREIGN_KEY REFERENCES Products(id)
        );
        """
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()
