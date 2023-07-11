"""
Setup functions for creating database and tables
"""
import sqlite3

DB_FILE_PATH = "PYTA05_sweet.db"


# Get connection to db
def get_db_connection(db_path=DB_FILE_PATH):
    connection = sqlite3.connect(db_path)
    return connection


# Create database and tables
def create_database(db_path=DB_FILE_PATH):
    # create database
    connection = sqlite3.connect(db_path)

    # create tables
    create_tables(connection)


def create_tables(connection):
    create_users_table(connection)
    create_products_table(connection)
    create_orders_table(connection)
    create_order_items_table(connection)


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
        id TEXT NOT NULL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
        );
        """
    )
    connection.commit()


def create_products_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
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
    )
    connection.commit()


def create_orders_table(connection):
    pass


def create_order_items_table(connection):
    pass
