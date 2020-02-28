from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.orderitems.routes import orderitems_routes

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

app.register_blueprint(orderitems_routes)