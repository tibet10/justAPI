from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .repository import InventoryRepository

class InventoryService:

    def getInventoryById(id):
        try:
            return InventoryRepository.getInventoryById(id)
        except Exception as ex:
            raise Exception(str(ex))

    def getUomByInventoryId(inventory_id):
        try:
            return InventoryRepository.getUomByInventoryId(inventory_id)
        except Exception as ex:
            raise Exception(str(ex))

    def getInventoryByPartNo(partNo):
        try:
            return InventoryRepository.getInventoryByPartNo(partNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def buildUomSellingPrices(inventory_id):
        
        try:
            result = {}
        
            uom = InventoryService.getUomByInventoryId(inventory_id)

            if(uom):                
                selling_price = []
                for i in range(len(uom.sell_prices)):
                    selling_price.insert(i, str(uom.sell_prices[i]))

                result["EA"] = {
                        "id": uom.id,
                        "sellPrices": selling_price
                }

                return result

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