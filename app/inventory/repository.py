from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .models import Inventory, InventoryUom
from ..database import session_scope

class InventoryRepository:

    def getInventoryByPartNo(partNo):
        try:
            with session_scope() as session:      

                inventory = session.query(Inventory)\
                                   .filter(Inventory.part_no == partNo) \
                                   .first()

                return inventory

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getInventoryById(id):
        try:
            with session_scope() as session:      

                inventory = session.query(Inventory)\
                                   .filter(Inventory.id == id) \
                                   .first()
                return inventory

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getUomByInventoryId(inventory_id):
        try:
            with session_scope() as session:      

                inventory = session.query(InventoryUom) \
                                   .join(Inventory, Inventory.id == InventoryUom.inventory_id) \
                                   .filter(Inventory.id == inventory_id, InventoryUom.uom == 'EA') \
                                   .first() 

                return inventory

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getRecentInventories(modified):
        try:
            with session_scope() as session:      

                    inventories = session.query(Inventory) \
                                         .filter(Inventory._modified > modified) \
                                         .all()
                                 
                    return inventories

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllInventories():
        try:
            with session_scope() as session:      

                    return session.query(Inventory) \
                                  .all()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None