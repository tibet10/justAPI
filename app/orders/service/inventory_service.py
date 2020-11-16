from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..repository.inventory_repository import InventoryRepository
from ...database import session_scope

class InventoryService:

    def createInventoryDetails(inventory):
        try:
            result = {
                "id": inventory.id,
                "whse": inventory.whse,
                "partNo": inventory.part_no,
                "description": inventory.description,
                "alternatePartNo": inventory.alt_part_no
            }            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None