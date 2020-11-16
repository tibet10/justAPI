from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..repository.order_items_repository import OrderItemRepository
from ...database import session_scope

class CustomerService:

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