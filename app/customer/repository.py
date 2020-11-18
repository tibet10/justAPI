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