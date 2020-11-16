from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps
from .models import SalesOrder, SalesOrderItem
from ..database import session_scope
from .service.order_service import OrderService
from .service.order_item_service import OrderItemService
from datetime import datetime
from . import orders_bp

@orders_bp.route('/sales/orders/GetSpireOrderDetail/<id>', methods=['GET'])
def GetSpireOrderDetailsById(id):
    
    try:
        
        sales_order = OrderService.getOrderById(id)

        #build order details
        result = OrderService.buildOrderDetails(sales_order)        

        return jsonify(result)  

    except Exception as ex:
        abort(404, description=str(ex))
        
    
@orders_bp.route('/sales/orders/GetAllSpireOrders', methods=['GET'])
def GetAllSpireOrders():
    result = []                
            
    try:
        with session_scope() as session:
        
            sales_orders = OrderService.getAllOrders()
            
            for row in sales_orders:
                result.append({
                    'id': row.SalesOrder.id,
                    'orderNo': row.SalesOrder.order_no,
                    'status': row.SalesOrder.status,
                    'orderDate': row.SalesOrder.order_date,
                    'created': row.SalesOrder._created,
                    'modified': row.SalesOrder._modified,
                    'modifiedBy': row.SalesOrder._modified_by,
                    'createdBy': row.SalesOrder._created_by,
                    'part_no': row.SalesOrderItem.part_no,
                    'salesOrder_id': row.SalesOrder.id,
                    'salesOrderItem_id': row.SalesOrderItem.id
                })

            return jsonify(result)  

    except Exception as ex:
        abort(404, description=str(ex))
        
    return result


@orders_bp.route('/sales/orders/GetNewSpireOrders', methods=['GET'])
def GetNewSpireOrders():    
    try:
        result = []  

        lastSynchronized = request.args.get('lastSynchronized')
        
        if not lastSynchronized:
            raise Exception("missing lastSynchronized")
        
        modified = datetime.strptime(lastSynchronized, '%m/%d/%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S %p') 
        
        sales_orders = OrderService.getRecentOrders(modified)

        for row in sales_orders:
                result.append({
                    'id': row.SalesOrder.id,
                    'orderNo': row.SalesOrder.order_no,
                    'status': row.SalesOrder.status,
                    'orderDate': row.SalesOrder.order_date,
                    'created': row.SalesOrder._created,
                    'modified': row.SalesOrder._modified,
                    'modifiedBy': row.SalesOrder._modified_by,
                    'createdBy': row.SalesOrder._created_by
                })

        return jsonify(result)  

    except Exception as e:
        abort(404, description=str(e))

    return result

@orders_bp.route('/sales/orders/GetDeletedSpireOrders', methods=['GET'])
def GetDeletedSpireOrders():
    try:
        result = [] 

        sales_orders = OrderService.getDeletedOrders()
        
        for sales_order in sales_orders:
                result.append({
                    'id': sales_order.id,
                    'orderNo': sales_order.order_no,
                    'status': sales_order.status,
                    'orderDate': sales_order.order_date,
                    'created': sales_order._created,
                    'modified': sales_order._modified,
                    'modifiedBy': sales_order._modified_by,
                    'createdBy': sales_order._created_by,
                    '_deleted': sales_order._deleted
                })

        return jsonify(result)  

    except Exception as e:
        abort(404, description=str(e))

    return result
