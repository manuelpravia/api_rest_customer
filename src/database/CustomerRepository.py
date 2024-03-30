import psycopg2
from psycopg2 import DatabaseError
from src.models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.connection = psycopg2.connect(database="springboot", user="postgres", password="contrasena", host="localhost", port="3432")

    def __del__(self):
        if self.connection:
            self.connection.close()
    
    def map_to_customer(self, row):
        print(row)
        id, names, surnames, document_type, document_number, email , phone, address  = row
        return Customer(id, names, surnames, document_type, document_number, address, phone, email)

    def get_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customer")
            customers = [self.map_to_customer(row) for row in cursor.fetchall()]
            cursor.close()
            return customers
        except DatabaseError as e:
            print(f"Error al obtener una lista de clientes: {e}")
            raise e

    def get_by_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM customer WHERE id = %s", (id,))
            customer_data = cursor.fetchone()
            cursor.close()
            if customer_data != None:
                customer = self.map_to_customer(customer_data)
                return customer
            else:
                return None           
        except DatabaseError as e:
            print(f"Error al obtener un cliente: {e}")
            raise e

    def create(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO customer (names, surnames, document_type, document_number, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id, names, surnames, document_type, document_number, address, phone, email", (data["names"], data["surnames"], data["document_type"], data["document_number"], data["address"], data["phone"], data["email"]))
            new_customer_data = cursor.fetchone()
            self.connection.commit()
            cursor.close()
            new_customer = self.map_to_customer(new_customer_data)
            return new_customer
        except DatabaseError as e:
            print(f"Error al crear cliente: {e}")
            raise e

    def update(self, id, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE customer SET names = %s, surnames = %s, document_type = %s, document_number = %s, address = %s, phone = %s, email = %s WHERE id = %s", (data["names"], data["surnames"], data["document_type"], data["document_number"], data["address"], data["phone"], data["email"], id))
            self.connection.commit()
            cursor.close()
            return self.get_by_id(id)
        except DatabaseError as e:
            print(f"Error al actualizar cliente: {e}")
            raise e

    def delete(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM customer WHERE id = %s", (id,))
            self.connection.commit()
            cursor.close()
        except  DatabaseError as e:
            print(f"Error al eliminar cliente")
            raise e

