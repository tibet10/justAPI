from flask import Blueprint, jsonify, request
from .models import SalesOrderItems

orderitems_routes = Blueprint('orderitems_routes', __name__)

# A route to return all of the available entries in our catalog.
@orderitems_routes.route('/api/orderitems/all', methods=['GET'])
def get_sales_order_items():
    items = SalesOrderItems.query.all()
    return jsonify({'items': list(map(lambda items: items.serialize(), items))})

# A route to return all of the available entries in our catalog.
@orderitems_routes.route('/api/orderitems/', methods=['GET'])
def get_sales_order_items_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    item = SalesOrderItems.query.get(id)

    return jsonify({'item': item.serialize()})

