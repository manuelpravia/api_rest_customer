
from src.database.CustomerRepository import CustomerRepository

class CustomerService:

    def __init__(self):
        self.customer_repository = CustomerRepository()

    def get_all(self):
        return self.customer_repository.get_all()

    def get_by_id(self,id):
        return self.customer_repository.get_by_id(id)

    def create(self, data):
        return self.customer_repository.create(data)

    def update(self, id, data):
        return self.customer_repository.update(id, data)


    def delete(self, id):
        return self.customer_repository.delete(id)