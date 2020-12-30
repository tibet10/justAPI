from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from sqlalchemy import or_, and_
from .models import SalesOrder, SalesOrderItem
from ..database import session_scope

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

    def getOrderByOrderNo(orderNo):
        try:
            with session_scope() as session:      

                    sales_order = session.query(SalesOrder) \
                                         .filter(SalesOrder.order_no == orderNo) \
                                         .first()
                    return sales_order

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllOrders():
        try:
            with session_scope() as session:      

                    sub_query = session.query(SalesOrderItem.order_no) \
                                       .group_by(SalesOrderItem.order_no) \
                                       .subquery() 
                    
                    sales_orders = session.query(SalesOrder, sub_query) \
                                          .join(sub_query, SalesOrder.order_no == sub_query.c.order_no) \
                                          .all()

                    return sales_orders

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getRecentOrders(modified):
        try:
            with session_scope() as session:      

                    sub_query = session.query(SalesOrderItem.order_no) \
                                       .filter(SalesOrderItem._modified > modified) \
                                       .group_by(SalesOrderItem.order_no) \
                                       .subquery() 
                    
                    sales_orders = session.query(SalesOrder, sub_query) \
                                          .join(sub_query, SalesOrder.order_no == sub_query.c.order_no) \
                                          .filter(SalesOrder._modified > modified) \
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

    def getOrderItemsByOrderNo(orderNo):
        try:
            with session_scope() as session:      

                sales_order_items = session.query(SalesOrderItem)\
                                           .filter(SalesOrderItem.order_no == orderNo) \
                                           .all()
                return sales_order_items

        except Exception as ex:
            raise Exception(str(ex))
        
        return None