from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .models import Inventory
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