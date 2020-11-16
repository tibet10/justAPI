from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..models import SalesOrder, SalesOrderItem
from ...database import session_scope

class OrderItemRepository:

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