from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .models import Customer
from ..database import session_scope

class CustomerRepository:

    def getCustomerByNo(custNo):
        try:
            with session_scope() as session:      

                customer = session.query(Customer)\
                                  .filter(Customer.cust_no == custNo) \
                                  .first()
                return customer

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getCustomerById(id):
        try:
            with session_scope() as session:      

                return session.query(Customer)\
                                   .filter(Customer.id == id) \
                                   .first()

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def getRecentCustomers(modified):
        try:
            with session_scope() as session:      

                    return session.query(Customer) \
                                  .filter(Customer.last_modified > modified) \
                                  .all()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllCustomers():
        try:
            with session_scope() as session:      

                    return session.query(Customer) \
                                  .all()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None