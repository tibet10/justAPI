from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from sqlalchemy import create_engine
import os

app = Flask(__name__)

class Database():
    def __init__(self, db_url=None):        
        self.db_url = db_url or os.getenv('SQLALCHEMY_DATABASE_URI')

        if not self.db_url:
            raise ValueError('You must provide db url')

        self.engine = create_engine(self.db_url)
    
    def get_connection(self):
        return Connection(self.engine.connect())

    def query(self, query):
        with self.get_connection() as conn:
            return conn.query(query)
    def __enter__(self):
        return self

    def __exit__(self, exc, val, traceback):
        self._engine.dispose()
    
class Connection():
    def __init__(self, connection):
        self._conn = connection

    def query(self, sql_query):
        return self._conn.execute(sql_query)
    
    def __enter__(self):
        return self

    def __exit__(self, exc, val, traceback):
        self._conn.close()  


@app.route('/', methods=['GET'])
def index():
    try:
        db = Database()
        result = db.query("SELECT id FROM sales_orders")
        for row in result:
            print("id:", row['id'])
    except Exception as ex:
        print(ex)

    return 'success'

