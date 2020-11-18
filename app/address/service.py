from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .repository import AddressRepository

class AddressService:

    def getBillingAddressByOrderNo(orderNo):
        try:
            return AddressRepository.getBillingAddressByOrderNo(orderNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getShippingAddressByOrderNo(orderNo):
        try:
            return AddressRepository.getShippingAddressByOrderNo(orderNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None
    
    def createBillingAddressDetails(address):
        try:
            result = {
                "id": address.id,
                "type": address.addr_type,
                "email": address.email,
                "city": address.city,
                "postalCode": address.postal_zip,
                "provState": address.prov_state,
                "country": address.country_code,
                "phone": {
                    "number": address.phone
                },
                "fax": {
                    "number": address.fax
                },
                "line1": address.address[0],
                "line2": address.address[1],
                "line3": address.address[2],
                "line4": address.address[3],
                "created": address._created,
                "modified": address._modified,
                "name": address.name
            }            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def createShippingAddressDetails(address):
        try:
            result = {
                "id": address.id,
                "type": address.addr_type,
                "email": address.email,
                "city": address.city,
                "postalCode": address.postal_zip,
                "provState": address.prov_state,
                "country": address.country_code,
                "phone": {
                    "number": address.phone
                },
                "fax": {
                    "number": address.fax
                },
                "line1": address.address[0],
                "line2": address.address[1],
                "line3": address.address[2],
                "line4": address.address[3],
                "created": address._created,
                "modified": address._modified,
                "name": address.name
            }            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None