from flask import Flask, jsonify, json, request, abort, render_template, Blueprint

from .repository import CustomerRepository

class CustomerService:

    def getCustomerByNo(custNo):
        try:
            return CustomerRepository.getCustomerByNo(custNo)

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def createCustomerDetails(customer):
        try:
            result = {
                "id": customer.id,
                "code": customer.cust_no,
                "customerNo": customer.cust_no,
                "name": customer.name
            }            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None