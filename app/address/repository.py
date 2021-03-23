from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .models import Address
from ..database import session_scope

class AddressRepository:
    
    def getBillingAddressByOrderNo(orderNo):
        try:
            with session_scope() as session:      

                    address = session.query(Address) \
                              .filter(Address.link_no == orderNo) \
                              .filter(Address.link_table == 'SORD') \
                              .filter(Address.addr_type == 'B') \
                              .first()
                    return address

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getShippingAddressByOrderNo(orderNo):
        try:
            with session_scope() as session:      

                    address = session.query(Address) \
                                         .filter(Address.link_no == orderNo) \
                                         .filter(Address.link_table == 'SORD') \
                                         .filter(Address.addr_type == 'S') \
                                         .first()
                    return address

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getEmailByCustomerNo(customerNo):
        try:
            with session_scope() as session:      

                    address = session.query(Address) \
                              .filter(Address.link_no == customerNo) \
                              .filter(Address.link_table == 'CUST') \
                              .filter(Address.addr_type == 'B') \
                              .first()
                    return address.email

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getCustomerBillingAddress(customerNo):
        try:
            with session_scope() as session:      

                    return session.query(Address) \
                              .filter(Address.link_no == customerNo) \
                              .filter(Address.link_table == 'CUST') \
                              .filter(Address.addr_type == 'B') \
                              .first()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllShippingAddressByCustNo(customerNo):
        try:
            with session_scope() as session:      

                   return session.query(Address) \
                                         .filter(Address.link_no == customerNo) \
                                         .filter(Address.link_table == 'CUST') \
                                         .filter(Address.addr_type == 'S') \
                                         .all()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAddressById(id):
        try:
            with session_scope() as session:      

                return session.query(Address)\
                                   .filter(Address.id == id) \
                                   .first()

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

