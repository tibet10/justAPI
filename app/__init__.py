from flask import Flask, Blueprint
from .orders.views import orders_bp

app = Flask(__name__) 

app.register_blueprint(orders_bp)