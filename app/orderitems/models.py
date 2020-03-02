from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

class SalesOrderItems(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    _modified = db.Column(db.DateTime())
    order_no = db.Column(db.String(100))

    def __init__(self, order_no):
        self.order_no = order_no

    def serialize(self):
        return {"id": self.id,
                "_modified": self._modified}


