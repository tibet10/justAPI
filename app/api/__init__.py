from flask import Blueprint

orders_bp = Blueprint('orders', __name__)
invoices_bp = Blueprint('invoices', __name__)
inventory_bp = Blueprint('inventory', __name__)
customer_bp = Blueprint('customer', __name__)