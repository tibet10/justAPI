from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from sqlalchemy import or_, and_
from ..models import SalesOrder, SalesOrderItem
from ...database import session_scope

class OrderRepository:

    def getOrderById(id):
        try:
            with session_scope() as session:      

                    sales_order = session.query(SalesOrder) \
                                        .filter(SalesOrder.id == id) \
                                        .first()
                    return sales_order

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllOrders():
        try:
            with session_scope() as session:      

                    sales_orders = session.query(SalesOrder, SalesOrderItem) \
                                  .join(SalesOrderItem, SalesOrder.order_no == SalesOrderItem.order_no) \
                                  .all()

                    return sales_orders

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    
    def getRecentOrders(modified):
        try:
            with session_scope() as session:      

                    sales_orders = session.query(SalesOrder, SalesOrderItem) \
                                  .join(SalesOrderItem, SalesOrder.order_no == SalesOrderItem.order_no) \
                                  .filter(or_(SalesOrder._modified > modified, SalesOrderItem._modified > modified)) \
                                  .filter(SalesOrder._deleted == None) \
                                  .all()
                                 
                    return sales_orders

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getDeletedOrders():
        try:
            with session_scope() as session:      

                    sales_order = session.query(SalesOrder) \
                                        .filter(SalesOrder._deleted != None) \
                                        .all()
                    return sales_order

        except Exception as ex:
           raise Exception(str(ex))
        
        return None