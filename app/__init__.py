from flask import Flask, Blueprint
from .api.orders import orders_bp
from .api.invoices import invoices_bp
from .errorhandler import errors_bp

app = Flask(__name__) 

app.register_blueprint(errors_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(invoices_bp)