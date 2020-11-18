from flask import Flask, Blueprint
from .api.orders import orders_bp

app = Flask(__name__) 

app.register_blueprint(orders_bp)