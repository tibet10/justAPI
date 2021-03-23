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
    
    def buildOrderAddress(address):
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

    def buildCustomerAddress(address):
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
                "name": address.name,
                "shipId": address.ship_id,
                "sellLevel": address.sell_no,
                "contacts": AddressService.buildCustomerContacts(address)
            }            
            return result

        except Exception as ex:
            raise Exception(str(ex))        
        return None

    def buildCustomerBillingAddress(address):
       return AddressService.buildCustomerAddress(address)

    def buildCustomerShippingAddresses(shipping_addresses):
        try:
            result = []  
            
            for address in shipping_addresses:
                result.append(AddressService.buildCustomerAddress(address))        
            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def buildCustomerContacts(address):
        try:

            result = []  
            
            for i in range(3):
                result.append({
                    "name": address.contact_name[i],
                    "email": address.contact_email[i],
                    "phone": {
                        "number": address.contact_phone[i],
                        "format": 1
                    },
                    "fax": {
                        "number": address.contact_fax[i],
                        "format": 1
                    },
                })        
            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getEmailByCustomerNo(customerNo):
        try:
            return AddressRepository.getEmailByCustomerNo(customerNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getCustomerBillingAddress(customerNo):
        try:
            return AddressRepository.getCustomerBillingAddress(customerNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None
    
    def getAllShippingAddressByCustNo(customerNo):
        try:
            return AddressRepository.getAllShippingAddressByCustNo(customerNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getAddressById(id):
        try:
            return AddressRepository.getAddressById(id)
        except Exception as ex:
            raise Exception(str(ex))
    