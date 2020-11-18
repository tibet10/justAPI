from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .repository import InventoryRepository

class InventoryService:

    def getInventoryByPartNo(partNo):
        try:
            return InventoryRepository.getInventoryByPartNo(partNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

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