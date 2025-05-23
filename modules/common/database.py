import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/viktoria/it_projects/QA_Auto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()


    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully.SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    # Метод отримання юзера по name
    def get_user_by_name(self, name):
        if name == '':
            raise Exception('Name is not provided')
        if not type(name) is str:
            raise TypeError('Name is not a string. Please, provide a string')

        query = f"SELECT name, address, city FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        user_data = self.cursor.fetchall()

        return user_data

     # Метод отримання юзера по id
    def get_user_by_id(self, id):
        if id == '':
            raise Exception('Id is incorrect')
        if not type(id) is int:
            raise TypeError('Id is not a integer. Please, provide a integer')
        
        query = f"SELECT id, name, address, city FROM customers WHERE id = '{id}'"
        self.cursor.execute(query)
        user_data = self.cursor.fetchall()

        return user_data

    
    # Метод додавання сustomers
    def insert_customers(self, customers_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address,city, postalCode, country) \
            VALUES ('{customers_id}', '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self,product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description,quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

            
