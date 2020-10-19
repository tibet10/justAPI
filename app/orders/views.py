from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps
from .models import SalesOrder, SalesOrderItem
from ..lib.utils import sqla2dict
from ..database import session_scope

from . import orders_bp

@orders_bp.route('/sales/orders/GetNewSpireOrders', methods=['GET'])
def GetNewSpireOrders():
    try:
        with session_scope() as session:
            # sales_orders = session.query(SalesOrder.order_no, SalesOrderItem.part_no, SalesOrderItem.id, SalesOrderItem.id) \
            #                       .select_from(SalesOrder) \
            #                       .join(SalesOrderItem, SalesOrder.order_no == SalesOrderItem.order_no) \
            #                       .filter(SalesOrder.order_no == '49') \
            #                       .all()
            # sales_orders = session.query(SalesOrder)


            # records = session.query(SalesOrder.order_no, SalesOrderItem.part_no, SalesOrderItem.id, SalesOrderItem.id).\
    	    #             join(SalesOrderItem, SalesOrder.order_no == SalesOrderItem.order_no).all()

            sales_orders = session.query(SalesOrder.order_no, SalesOrderItem.part_no, SalesOrderItem.id, SalesOrderItem.id) \
                                  .select_from(SalesOrder) \
                                  .join(SalesOrderItem, SalesOrder.order_no == SalesOrderItem.order_no) \
                                  .filter(SalesOrderItem.part_no == "PUMA") \
                                  .all()
            my_list = []                
            for record in sales_orders:
                my_list.append({
                    'order_no': record.order_no,
                    'part_no': record.part_no,
                    'salesOrder_id': record.id,
                    'SalesOrderItem_id': record.id
                })
            print(my_list)
            return jsonify(my_list)

    except Exception as ex:
        print(ex)
        
    return "fail"
