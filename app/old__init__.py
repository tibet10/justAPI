from flask import Flask, jsonify, json, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,
from datetime import datetime
import os

app = Flask(__name__)

class Database():
    def __init__(self, db_url=None):   
        self.db_url = db_url or os.getenv('SQLALCHEMY_DATABASE_URI_UAT_2')

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

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/sales/orders/GetNewSpireOrders', methods=['GET'])
def GetNewSpireOrders():
    try:
        lastSynchronized = request.args.get('lastSynchronized')
        
        if not lastSynchronized:
            raise Exception("missing lastSynchronized")
        
        modified = datetime.strptime(lastSynchronized, '%m/%d/%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S %p') 
        
        db = Database() 

        result = db.query("SELECT sales_orders.id, sales_orders.order_no AS orderNo, sales_orders.status, " + 
                          "sales_orders.order_date AS orderDate, sales_orders._created AS created, " +
                          "sales_orders._modified AS modified, sales_orders._modified_by AS modifiedBy, " +
                          "sales_orders._created_by AS createdBy " + 
                          "FROM sales_orders " + 
                          "LEFT JOIN sales_order_items ON sales_orders.id = CAST (sales_order_items.order_no AS INTEGER) " + 
                          "WHERE (sales_orders._modified > '" + modified + "' OR " + 
                          "sales_order_items._modified > '" + modified + "') " + 
                          "AND sales_orders._deleted is null")
        
        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result

@app.route('/sales/orders/GetDeletedSpireOrders', methods=['GET'])
def GetDeletedSpireOrders():
    try:
        db = Database() 

        result = db.query("SELECT _deleted, sales_orders.id, sales_orders.order_no AS orderNo, sales_orders.status, " + 
                          "sales_orders.order_date AS orderDate, sales_orders._created AS created, " + 
                          "sales_orders._modified AS modified, sales_orders._modified_by AS modifiedBy, " + 
                          "sales_orders._created_by AS createdBy " + 
                          "FROM sales_orders " + 
                          "WHERE sales_orders._deleted is not null")

        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result

@app.route('/sales/invoices/GetNewSpireInvoices', methods=['GET'])
def GetNewSpireInvoices():
    try:
        lastSynchronized = request.args.get('lastSynchronized')
        
        if not lastSynchronized:
            raise Exception("missing lastSynchronized")
        
        modified = datetime.strptime(lastSynchronized, '%m/%d/%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S %p') 
        
        db = Database() 

        result = db.query("SELECT id, invoice_no AS invoiceNo, invoice_date AS invoiceDate, order_no AS orderNo, " + 
                          "division, location, profit_center AS profitCenter,order_date AS orderDate,required_date AS requiredDate, " +
                          "_created AS created,_modified AS modified,_created_by AS createdBy,_modified_by AS modifiedBy " + 
                          "FROM sales_history " +
                          "WHERE sales_history._modified > '" + modified + "'")

        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result

@app.route('/sales/invoices/GetAllSpireInvoices', methods=['GET'])
def GetAllSpireInvoices():
    try:
        db = Database() 

        result = db.query("SELECT id, invoice_no AS invoiceNo, invoice_date AS invoiceDate, order_no AS orderNo, " + 
                          "division, location, profit_center AS profitCenter,order_date AS orderDate,required_date AS requiredDate, " +
                          "_created AS created,_modified AS modified,_created_by AS createdBy,_modified_by AS modifiedBy " + 
                          "FROM sales_history ")

        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result

@app.route('/sales/orders/GetAllSpireOrders', methods=['GET'])
def GetAllSpireOrders():
    try:
        db = Database() 

        result = db.query("SELECT sales_orders.id, sales_orders.order_no AS orderNo, sales_orders.status, " + 
                          "sales_orders.order_date AS orderDate, sales_orders._created AS created, " +
                          "sales_orders._modified AS modified, sales_orders._modified_by AS modifiedBy, " +
                          "sales_orders._created_by AS createdBy " + 
                          "FROM sales_orders " + 
                          "LEFT JOIN sales_order_items ON sales_orders.id = CAST (sales_order_items.order_no AS INTEGER) " +
                          "WHERE sales_orders._deleted is null")
        
        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result

@app.route('/sales/orders/GetSpireOrderByOrderNumber', methods=['GET'])
def GetSpireOrderByOrderNumber():
    try:
        orderNumber = request.args.get('orderNumber')

        db = Database() 

        result = db.query("SELECT sales_orders.id, sales_orders.order_no AS orderNo, sales_orders.status, " + 
                          "sales_orders.order_date AS orderDate, sales_orders._created AS created, " +
                          "sales_orders._modified AS modified, sales_orders._modified_by AS modifiedBy, " +
                          "sales_orders._created_by AS createdBy " + 
                          "FROM sales_orders " + 
                          "WHERE sales_orders.order_no = '" + orderNumber + "' LIMIT 1")
        
        json_result = jsonify([dict(r) for r in result])

    except Exception as e:
        abort(404, description=str(e))

    return json_result