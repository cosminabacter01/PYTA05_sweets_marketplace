"""
DB CRUD methods for Products table
"""
import json
from db.crud.interface_crud import CrudABC


class ProductsDb(CrudABC):

    def create(self, entry_to_create):
        pass

    def read(self, id=None):
        sql_query = "SELECT * FROM Products "
        value = ''
        if id:
            sql_query += "WHERE id=?;"
            value = id
        cursor = self.connection.cursor()
        if not value:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, (value,))

        products = cursor.fetchall()  # o lista cu liste

        products_json = []
        for product in products:
            products_json.append({
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "ingredients": product[3],
                "price": product[4],
                "weight_grams": product[5],
                "available_quantity": product[6],
                "image": product[7]
            })
        return products_json

    def update(self, entry_for_update):
        pass

    def delete(self, id):
        pass

    def setup_products(self, source_path):
        cursor = self.connection.cursor()
        cursor.execute("""
        SELECT * FROM Products;
        """)
        if not cursor.fetchone():
            with open(source_path, mode="r") as f:
                products = json.load(f)
                table_data = [
                    (
                        product['name'],
                        product['description'],
                        product['ingredients'],
                        product['price'],
                        product['weight_grams'],
                        product['available_quantity'],
                        product['image']
                    ) for product in products]
                query = """
                INSERT INTO Products (name, description, ingredients, price, weight_grams, available_quantity, image)
                VALUES (?, ?, ?, ?, ?, ?, ?); 
                """
                cursor.executemany(query, table_data)
                self.connection.commit()
