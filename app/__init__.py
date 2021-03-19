from flask import Flask, Blueprint
from .api.orders import orders_bp
from .api.invoices import invoices_bp
from .api.inventory import inventory_bp
from .api.customer import customer_bp
from .errorhandler import errors_bp

app = Flask(__name__) 

app.register_blueprint(errors_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(invoices_bp)