from flask import Flask, jsonify, json, request, abort, render_template, Blueprint, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps
from datetime import datetime

from ..database import session_scope
from ..inventory.service import InventoryService
from ..orders.service import OrderService
from . import inventory_bp

@inventory_bp.route('/inventory/items/GetInventoryById/<id>', methods=['GET'])
def GetInventoryById(id):
    
    try:    
        result = {}

        inventory = InventoryService.getInventoryById(id)

        if inventory: 
            result['id']= inventory.id
            result['whse'] = inventory.whse
            result['productCode'] = inventory.product_code
            result['partNo'] = inventory.part_no 
            result['description'] = inventory.description
            result['alternatePartNo'] = inventory.alt_part_no
            result['extendedDescription'] = inventory.extended_description
            result['minimumBuyQty'] = str(inventory.min_buy_qty)
            result['purchaseQty'] = str(inventory.purchase_qty)
            result['created'] = inventory._created
            result['modified'] = inventory._modified
            result['createdBy'] = inventory._created_by
            result['modifiedBy'] = inventory._modified_by
            result['status'] = inventory.hold  
            result['pricing'] = InventoryService.buildUomSellingPrices(inventory.id)

        return Response(status=200, mimetype='application/json', response= json.dumps(result) if result else 'null')

    except Exception as ex:
        abort(404, description=str(ex))

@inventory_bp.route('/inventory/items/GetInventoryByPartNo', methods=['GET'])
def GetInventoryByPartNo():
    
    try:    
        result = {}

        partNo = request.args.get('partNo')

        inventory = InventoryService.getInventoryByPartNo(partNo)
        
        if inventory: 
            result['id']= inventory.id
            result['whse'] = inventory.whse
            result['productCode'] = inventory.product_code
            result['partNo'] = inventory.part_no 
            result['description'] = inventory.description
            result['alternatePartNo'] = inventory.alt_part_no
            result['extendedDescription'] = inventory.extended_description
            result['minimumBuyQty'] = str(inventory.min_buy_qty)
            result['purchaseQty'] = str(inventory.purchase_qty)
            result['created'] = inventory._created
            result['modified'] = inventory._modified
            result['createdBy'] = inventory._created_by
            result['modifiedBy'] = inventory._modified_by
            result['status'] = inventory.hold  
            result['pricing'] = InventoryService.buildUomSellingPrices(inventory.id)

        return Response(status=200, mimetype='application/json', response= json.dumps(result) if result else 'null')

    except Exception as ex:
        abort(404, description=str(ex))