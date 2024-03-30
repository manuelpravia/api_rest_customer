from flask import request, jsonify
from src.services.CustomerService import CustomerService

class CustomerController:

    def __init__(self):
        self.customer_service = CustomerService()

    def get_all(self):
        customers = self.customer_service.get_all()
        serialized_customers = [customer.to_dict() for customer in customers]
        return jsonify(serialized_customers)

    def get_by_id(self, id):
        customer = self.customer_service.get_by_id(id)
        if customer is None:
            return jsonify({"message": "Cliente no encontrado"}), 404
        return jsonify(customer.to_dict())

    def create(self):
        data = request.get_json()
        customer = self.customer_service.create(data)
        return jsonify(customer.to_dict()), 201

    def update(self, id):
        data = request.get_json()
        customer = self.customer_service.update(id, data)
        if customer is None:
            return jsonify({"message": "Cliente no encontrado"}), 404
        return jsonify(customer.to_dict())

    def delete(self, id):
        customer = self.customer_service.delete(id)
        if customer is None:
            return jsonify({"message": "Cliente no encontrado"}), 404
        return jsonify({"message": "Cliente eliminado"}), 200
