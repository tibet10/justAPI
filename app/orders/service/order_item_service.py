from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..repository.order_items_repository import OrderItemRepository
from ..repository.inventory_repository import InventoryRepository
from ..service.inventory_service import InventoryService
from ...database import session_scope

class OrderItemService:

    def createOrderItemDetails(sales_order_items):
        try:
            result = []

            for row in sales_order_items:

                inventory = InventoryRepository.getInventoryByPartNo(row.part_no)
                
                result.append({
                    'id': row.id,
                    'partNo': row.part_no,
                    'description': row.description,
                    'orderQty': int(row.order_qty),
                    'unitPrice': str(row.unit_price),
                    'inventory': InventoryService.createInventoryDetails(inventory) if inventory != None else None,
                    'retailPrice': str(row.retail_price),
                    'vendor': row.vendor_no,
                    'sequence': row.sequence
                })
            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return result