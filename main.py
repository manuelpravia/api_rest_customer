from flask import Flask
from src.routes.CustomerController import CustomerController

app = Flask(__name__)

controller = CustomerController()

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/database'

@app.route('/customers', methods=['GET'])
def get_all_customers():
    return controller.get_all()

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    return controller.get_by_id(id)

@app.route('/customers', methods=['POST'])
def create():
    return controller.create()

@app.route('/customers/<int:id>', methods=['PUT'])
def update(id):
    return controller.update(id)

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)



if __name__ == '__main__':
    app.run(debug=True) 


   